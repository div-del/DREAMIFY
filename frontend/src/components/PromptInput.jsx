import { useState } from "react";
import { motion } from "framer-motion";
import { Wand2 } from "lucide-react";

export function PromptInput({ onGenerate, isLoading }) {
    const [prompt, setPrompt] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (prompt.trim()) {
            onGenerate(prompt);
        }
    };

    return (
        <motion.form
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            onSubmit={handleSubmit}
            className="w-full max-w-2xl mx-auto px-4"
        >
            <div className="relative flex items-center bg-jungle-dark/40 backdrop-blur-md rounded-xl p-2 border border-biolum-green/20 box-shadow-lg shadow-biolum-green/10">
                <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Describe your dream image..."
                    disabled={isLoading}
                    className="w-full bg-transparent border-none text-white placeholder-gray-400 focus:ring-0 px-4 py-3 text-lg outline-none"
                />
                <button
                    type="submit"
                    disabled={isLoading || !prompt.trim()}
                    className="primary-btn rounded-xl px-6 py-3 flex items-center gap-2 min-w-[140px] justify-center ml-2"
                >
                    {isLoading ? (
                        <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                    ) : (
                        <>
                            <Wand2 size={20} />
                            <span>Generate</span>
                        </>
                    )}
                </button>
            </div>
        </motion.form>
    );
}
