/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                jungle: {
                    dark: "#0f1c15",
                    light: "#183325",
                },
                biolum: {
                    blue: "#00ffcc",
                    green: "#5eff5e",
                }
            },
            fontFamily: {
                dream: ['"Outfit"', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
