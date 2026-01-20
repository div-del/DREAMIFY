import { useState } from "react";
import axios from "axios";
// import { Hero } from "./components/Hero"; // Unused
import { PromptInput } from "./components/PromptInput";
import { ImageDisplay } from "./components/ImageDisplay";

function App() {
  const [image, setImage] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerate = async (prompt) => {
    setIsLoading(true);
    setImage(null);
    try {
      // Use 127.0.0.1 to avoid localhost IPv6 issues
      const response = await axios.post("http://127.0.0.1:8000/api/generate-video", {
        prompt: prompt,
      });
      console.log("Response data:", response.data);
      if (response.data.image) {
        setImage(response.data.image);
      } else {
        throw new Error("No image data in response");
      }
    } catch (error) {
      console.error("Error generating video:", error);
      alert(`Failed to generate video: ${error.message}. Check backend console.`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full relative flex flex-col items-center justify-center p-4 overflow-hidden">
      {/* Overlay to darken background slightly for readability and add misty vibe */}
      <div className="absolute inset-0 bg-jungle-dark/60 pointer-events-none backdrop-blur-[1px]"></div>

      <div className="container max-w-4xl mx-auto z-10 flex flex-col items-center gap-10">
        {/* Title */}
        <div className="text-center space-y-6 mt-12 mb-8">
          <h1 className="text-8xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-cyan-200 to-teal-400 font-dream tracking-tighter drop-shadow-[0_0_25px_rgba(45,212,191,0.5)]">
            Dreamify
          </h1>
          <p className="text-teal-200 text-xl tracking-widest font-semibold drop-shadow-md">
            WELCOME TO DREAMIFY! GIVE PROMPT AND GET GIF!
          </p>
        </div>

        {/* Input Section */}
        <div className="w-full max-w-2xl glass-panel p-8 backdrop-blur-md">
          <PromptInput onGenerate={handleGenerate} isLoading={isLoading} />
        </div>

        {/* Display Section */}
        <div className="w-full flex justify-center mt-4">
          {/* Pass image to ImageDisplay. If it's a GIF from backend, it works same as image source */}
          <ImageDisplay image={image} isLoading={isLoading} />
        </div>
      </div>
    </div>
  );
}

export default App;
