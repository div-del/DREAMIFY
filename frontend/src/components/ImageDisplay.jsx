import { motion, AnimatePresence } from "framer-motion";
import { Download, Maximize2 } from "lucide-react";

export function ImageDisplay({ image, isLoading }) {
    if (!image && !isLoading) return null;

    return (
        <div className="w-full max-w-2xl mx-auto mt-12 px-4 pb-12">
            <div className="aspect-square w-full rounded-2xl overflow-hidden glass-panel relative flex items-center justify-center">
                <AnimatePresence mode="wait">
                    {isLoading ? (
                        <motion.div
                            key="loader"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="flex flex-col items-center gap-4"
                        >
                            <div className="w-16 h-16 rounded-full border-4 border-biolum-blue border-t-biolum-green animate-spin" />
                            <p className="text-biolum-blue animate-pulse font-medium text-lg">Dreaming up your GIF (generating frames)...</p>
                        </motion.div>
                    ) : (
                        image && (
                            <motion.div
                                key="image"
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ type: "spring", stiffness: 100 }}
                                className="relative w-full h-full group"
                            >
                                <img
                                    src={image}
                                    alt="Generated Dream"
                                    className="w-full h-full object-cover"
                                />
                                <div className="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-4 backdrop-blur-sm">
                                    <a
                                        href={image}
                                        download="dream.gif"
                                        className="p-3 bg-white/10 hover:bg-white/20 rounded-full text-white transition-colors"
                                        title="Download"
                                    >
                                        <Download size={24} />
                                    </a>
                                    <button
                                        onClick={() => window.open(image, "_blank")}
                                        className="p-3 bg-white/10 hover:bg-white/20 rounded-full text-white transition-colors"
                                        title="View Full Size"
                                    >
                                        <Maximize2 size={24} />
                                    </button>
                                </div>
                            </motion.div>
                        )
                    )}
                </AnimatePresence>
            </div>
        </div>
    );
}
