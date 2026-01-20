import os
import io
import base64
import time
import random
import traceback
from pathlib import Path
from PIL import Image
from .generator import ImageGenerator

class VideoGenerator:
    def __init__(self):
        print("DEBUG: VideoGenerator INITIALIZED (v3 - debug)", flush=True)
        self.image_generator = ImageGenerator()
        # Ensure we have a temp directory
        self.temp_dir = Path("temp_frames")
        self.temp_dir.mkdir(exist_ok=True)

    def generate_gif(self, prompt: str, num_frames: int = 5, fps: int = 2):
        """
        Generates a GIF from N unique frames based on the prompt.
        Returns base64 encoded string of the GIF.
        """
        pil_frames = []  # Store PIL images for GIF creation
        
        print(f"Starting video generation for: {prompt}", flush=True)
        
        # Frame variation words to append for generating distinct frames
        frame_variations = [
            "beginning of scene",
            "scene in motion",
            "mid-action moment",
            "dynamic transition",
            "scene conclusion"
        ]
        
        try:
            for i in range(num_frames):
                # Add variation to the prompt to force different outputs
                varied_prompt = f"{prompt}, {frame_variations[i % len(frame_variations)]}, frame {i+1}"
                print(f"Generating frame {i+1}/{num_frames} with prompt: {varied_prompt[:50]}...", flush=True)
                
                # Small delay to prevent rate limits
                if i > 0:
                    time.sleep(0.5)
                
                # Use random seed for variation
                seed = random.randint(0, 2**31 - 1)
                print(f"Using seed: {seed}", flush=True)
                image_base64, error = self.image_generator.generate(varied_prompt, seed=seed)
                
                if error:
                    print(f"Error generating frame {i+1}: {error}")
                    # If we have at least 1 image, we can try to make a GIF, but better to fail?
                    # Let's try to proceed if we have at least 3 frames, otherwise abort.
                    if len(pil_frames) < 3:
                        return None, f"Failed to generate enough frames. Stopped at {i+1}. Last error: {error}"
                    break
                
                # Decode to PIL Image directly
                image_data = base64.b64decode(image_base64)
                pil_img = Image.open(io.BytesIO(image_data)).convert('RGB')
                pil_frames.append(pil_img)
                print(f"Frame {i+1} generated successfully, size: {pil_img.size}", flush=True)
            
            if not pil_frames:
                return None, "No frames generated."

            print(f"Stitching {len(pil_frames)} frames into GIF using Pillow...", flush=True)
            
            # Create GIF using Pillow (more reliable)
            output_path = self.temp_dir / f"output_{int(time.time())}.gif"
            duration_ms = int(1000 / fps)  # Convert fps to milliseconds per frame
            
            # Save GIF with Pillow
            pil_frames[0].save(
                output_path,
                save_all=True,
                append_images=pil_frames[1:],
                duration=duration_ms,
                loop=0,  # 0 means infinite loop
                optimize=True
            )
            
            print(f"GIF saved to {output_path}", flush=True)
            
            # Read back as base64
            with open(output_path, "rb") as f:
                gif_bytes = f.read()
                gif_base64 = base64.b64encode(gif_bytes).decode('utf-8')
            
            # Cleanup
            try:
                os.remove(output_path)
            except:
                pass
                
            return gif_base64, None

        except Exception as e:
            print(f"Critical error in generate_gif: {e}", flush=True)
            traceback.print_exc()
            return None, str(e)
