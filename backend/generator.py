import os
import time
import sys
import requests
import base64
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the same directory as this file (backend/)
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

class ImageGenerator:
    def __init__(self):
        # List of reliable models to try
        self.models = [
            "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell",
            "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3.5-large",
            "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-2-1"
        ]
        self.current_model_index = 0
        self.api_url = self.models[0]
        self.api_token = os.getenv("HF_TOKEN")
        
        if not self.api_token:
            print(f"DEBUG: Current working directory: {os.getcwd()}", flush=True)
            print(f"DEBUG: Env path being checked: {env_path}", flush=True)
            print(f"DEBUG: HF_TOKEN env var: {os.environ.get('HF_TOKEN')}", flush=True)
            print("WARNING: HF_TOKEN is missing in .env file! Image generation will fail.", file=sys.stderr, flush=True)
        else:
            print(f"ImageGenerator initialized with Cloud API. Token found (length: {len(self.api_token)})", flush=True)

    def generate(self, prompt: str, seed: int = None):
        with open("debug_entry.txt", "w") as f:
            f.write(f"Entered generate with prompt: {prompt}")
        # Re-attempt loading env var if missing (debugging purpose)
        if not self.api_token:
            print(f"DEBUG RE-CHECK: Current CWD: {os.getcwd()}", flush=True)
            env_path = Path(__file__).parent / ".env"
            print(f"DEBUG RE-CHECK: Loading from {env_path}", flush=True)
            load_dotenv(dotenv_path=env_path)
            self.api_token = os.getenv("HF_TOKEN")
            print(f"DEBUG RE-CHECK: Token found? {bool(self.api_token)}", flush=True)

        if not self.api_token:
            print("Error: No HF_TOKEN found.", file=sys.stderr, flush=True)
            return None, "Error: No HF_TOKEN found in .env"

        headers = {"Authorization": f"Bearer {self.api_token}"}
        # Add random seed to parameters to ensure variation if requested
        import random
        if seed is None:
            seed = random.randint(0, 2**32 - 1)
            
        payload = {
            "inputs": prompt,
            "parameters": {"seed": seed}
        }

        print(f"Sending request to Hugging Face API for prompt: {prompt}", flush=True)
        
        # Retry with model fallback
        for model_url in self.models:
            print(f"Trying model: {model_url}", flush=True)
            self.api_url = model_url
            
            # Retry loop for model loading/timeouts per model
            for _ in range(3):
                try:
                    response = requests.post(self.api_url, headers=headers, json=payload)
                    
                    response_json = None
                    try:
                        response_json = response.json()
                    except:
                        pass

                    if response.status_code == 200:
                        image_bytes = response.content
                        image_base64 = base64.b64encode(image_bytes).decode()
                        return image_base64, None
                    
                    elif response_json and "estimated_time" in response_json:
                        wait_time = response_json["estimated_time"]
                        msg = f"Model is loading... waiting {wait_time} s"
                        print(msg, flush=True)
                        time.sleep(wait_time)
                        continue
                    
                    else:
                        error_msg = f"Model {model_url} failed: {response.status_code} - {response.text}"
                        print(error_msg, flush=True)
                        # return None, error_msg # Let it loop to next model
                        break # Break inner loop to try next model
                        
                except Exception as e:
                    print(f"CRITICAL EXCEPTION in generate: {e}", flush=True)
                    # Exfiltrate error if all fail, but for now continue
                    break 
        
        return None, "All models failed. Check token/quota."
