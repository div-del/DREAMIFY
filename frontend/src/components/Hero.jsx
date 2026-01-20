import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";

export function Hero() {
  return (
    <div className="text-center py-12 px-4">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="flex justify-center items-center gap-3 mb-4"
      >
        <Sparkles className="w-8 h-8 text-purple-400" />
        <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
          Dreamify
        </h1>
        <Sparkles className="w-8 h-8 text-pink-600" />
      </motion.div>
      
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3, duration: 0.8 }}
        className="text-lg text-gray-300 max-w-xl mx-auto"
      >
        Transform your imagination into reality with our premium AI image generator.
        Simply describe your dream, and watch it come to life.
      </motion.p>
    </div>
  );
}
