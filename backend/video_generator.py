import os
import io
import base64
import time
import tempfile
import traceback
from pathlib import Path
try:
    from moviepy.editor import ImageSequenceClip
except ImportError:
    from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
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
        frames_files = []
        
        print(f"Starting video generation for: {prompt}", flush=True)
        
        try:
            for i in range(num_frames):
                # We add a slight variation to the prompt or rely on API randomness. 
                print(f"Generating frame {i+1}/{num_frames}...", flush=True)
                
                # Small delay to prevent rate limits and ensure seed change if time-based
                # Small delay to prevent rate limits and ensure seed change if time-based
                if i > 0:
                    time.sleep(1)
                
                # Use loop index + time as seed factor for distinct frames
                import random
                seed = random.randint(0, 1000000) + i
                image_base64, error = self.image_generator.generate(prompt, seed=seed)
                
                if error:
                    print(f"Error generating frame {i+1}: {error}")
                    # If we have at least 1 image, we can try to make a GIF, but better to fail?
                    # Let's try to proceed if we have at least 3 frames, otherwise abort.
                    if len(frames_files) < 3:
                        return None, f"Failed to generate enough frames. Stopped at {i+1}. Last error: {error}"
                    break
                
                # Decode and save to temp file
                image_data = base64.b64decode(image_base64)
                frame_path = self.temp_dir / f"frame_{int(time.time())}_{i}.png"
                
                with open(frame_path, "wb") as f:
                    f.write(image_data)
                
                frames_files.append(str(frame_path))
            
            if not frames_files:
                return None, "No frames generated."

            print(f"Stitching {len(frames_files)} frames into GIF...", flush=True)
            
            # Create GIF using moviepy
            clip = ImageSequenceClip(frames_files, fps=fps)
            
            # Save to buffer
            output_path = self.temp_dir / f"output_{int(time.time())}.gif"
            print(f"Writing GIF to {output_path}...", flush=True)
            clip.write_gif(output_path, logger=None)
            
            # Read back as base64
            with open(output_path, "rb") as f:
                gif_bytes = f.read()
                gif_base64 = base64.b64encode(gif_bytes).decode('utf-8')
            
            # Cleanup temp files
            # (Optional: keep them for debugging)
            for f in frames_files:
                try:
                    os.remove(f)
                except:
                    pass
            try:
                os.remove(output_path)
            except:
                pass
                
            return gif_base64, None

        except Exception as e:
            print(f"Critical error in generate_gif: {e}", flush=True)
            traceback.print_exc()
            return None, str(e)
