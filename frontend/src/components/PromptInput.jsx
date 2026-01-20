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
            <div className="relative flex items-center gap-4 p-4 rounded-2xl bg-black/60 backdrop-blur-lg border-2 border-white/40">
                <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="✨ Describe your dream GIF..."
                    disabled={isLoading}
                    className="neon-input w-full rounded-xl px-6 py-5 text-xl"
                />
                <button
                    type="submit"
                    disabled={isLoading || !prompt.trim()}
                    className="neon-button rounded-xl px-8 py-5 flex items-center gap-3 min-w-[180px] justify-center text-xl"
                >
                    {isLoading ? (
                        <div className="w-7 h-7 border-3 border-white border-t-transparent rounded-full animate-spin" />
                    ) : (
                        <>
                            <Wand2 size={26} />
                            <span>Generate</span>
                        </>
                    )}
                </button>
            </div>
        </motion.form>
    );
}
