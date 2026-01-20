from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .generator import ImageGenerator
from .video_generator import VideoGenerator
import uvicorn
import os
import sys

app = FastAPI(title="Dreamify API", description="Backend for Dreamify Text-to-Image", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global generator instance
import inspect
print(f"DEBUG: ImageGenerator loaded from: {inspect.getfile(ImageGenerator)}", flush=True)
generator = ImageGenerator()
video_generator = VideoGenerator()

class PromptRequest(BaseModel):
    prompt: str

@app.on_event("startup")
async def startup_event():
    # Preload model on startup to make first request faster
    # verify if we should autoload. For now, let's load on first request to speed up server start for the user
    pass

@app.get("/")
def read_root():
    return {"message": "Dreamify Backend is running!"}

@app.post("/api/generate")
def generate_image(request: PromptRequest):
    try:
        print(f"Received request for prompt: {request.prompt}", flush=True)
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
        
        print("Calling generator...", flush=True)
            
        img_data, error = generator.generate(request.prompt)
        print("Generation complete", flush=True)
        if img_data is None:
            with open("last_error.txt", "w") as f:
                f.write(str(error))
            raise HTTPException(status_code=500, detail=f"Generation failed: {error}")
        
        return {"image": f"data:image/png;base64,{img_data}"}
        return {"image": f"data:image/png;base64,{img_data}"}
    except Exception as e:
        with open("last_error.txt", "w") as f:
            f.write(str(e))
        print(f"CRITICAL ERROR: {str(e)}", file=sys.stderr, flush=True)
        # traceback.print_exc(file=sys.stderr)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-video")
def generate_video(request: PromptRequest):
    try:
        print(f"Received VIDEO request for prompt: {request.prompt}", flush=True)
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
        
        print("Calling video generator...", flush=True)
            
        # Generate GIF (5 frames, 2 fps = 2.5 seconds approx)
        gif_data, error = video_generator.generate_gif(request.prompt, num_frames=5, fps=2)
        
        print("Video generation complete", flush=True)
        
        if gif_data is None:
            raise HTTPException(status_code=500, detail=f"Video generation failed: {error}")
        
        return {"image": f"data:image/gif;base64,{gif_data}", "type": "gif"}
    except Exception as e:
        print(f"CRITICAL VIDEO ERROR: {str(e)}", file=sys.stderr, flush=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
