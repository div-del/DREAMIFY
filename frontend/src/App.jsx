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
      {/* Overlay to darken background for better readability */}
      <div className="absolute inset-0 bg-black/70 pointer-events-none backdrop-blur-[2px]"></div>

      <div className="z-10 flex flex-col items-center justify-center w-full max-w-4xl">
        {/* Title Section - Centered */}
        <div className="text-center mb-10">
          <h1 className="text-8xl md:text-9xl font-bold neon-text font-dream tracking-tight mb-6">
            Dreamify
          </h1>
          <p className="text-white text-2xl md:text-3xl font-semibold tracking-wide mb-3 neon-glow">
            ✨ WELCOME TO DREAMIFY! ✨
          </p>
          <p className="text-white/80 text-lg md:text-xl tracking-widest">
            🎬 give prompt and get gif! 🎬
          </p>
        </div>

        {/* Prompt Input + Button Section - Horizontal Layout */}
        <div className="w-full max-w-2xl mb-6">
          <PromptInput onGenerate={handleGenerate} isLoading={isLoading} />
        </div>

        {/* Display Section */}
        <div className="w-full flex justify-center">
          <ImageDisplay image={image} isLoading={isLoading} />
        </div>
      </div>
    </div>
  );
}

export default App;
