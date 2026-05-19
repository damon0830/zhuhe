import type { Config } from "tailwindcss";
export default <Config>{
  content: ["./pages/**/*.{vue,js,ts}", "./components/**/*.{vue,js,ts}", "./app.vue"],
  theme: {
    extend: {
      colors: {
        navy: { DEFAULT: "#2D2D69", 50: "#E8E8F3", 100: "#C3C3E1", 200: "#9E9ECF", 300: "#7A7ABD", 400: "#5555AB", 500: "#2D2D69", 600: "#242455", 700: "#1B1B41", 800: "#12122D", 900: "#090919" },
        lake: { DEFAULT: "#B0E8E8", 50: "#F0FBFB", 100: "#DCF5F5", 200: "#C8EFEF", 300: "#B0E8E8", 400: "#85DCDC", 500: "#5AD0D0", 600: "#36C4C4", 700: "#2A9E9E", 800: "#1F7878", 900: "#145252" },
        lavender: { DEFAULT: "#C3C3E1", 50: "#F4F4FA", 100: "#E8E8F5", 200: "#D8D8EF", 300: "#C3C3E1", 400: "#A3A3D3", 500: "#8383C5", 600: "#6363B7", 700: "#4D4D9B", 800: "#3A3A79", 900: "#272757" },
        sandy: { DEFAULT: "#D4BFA5", 50: "#F8F4EF", 100: "#EFE8DD", 200: "#E2D6C5", 300: "#D4BFA5", 400: "#C4A883", 500: "#B49161", 600: "#9E7A4C", 700: "#7D603B", 800: "#5C462B", 900: "#3B2C1B" },
        cream: { DEFAULT: "#F5F0E8", 50: "#FEFDFC", 100: "#FAF7F2", 200: "#F5F0E8", 300: "#EDE4D4", 400: "#E5D8C0", 500: "#DDCCAC", 600: "#C9AE82", 700: "#B59058", 800: "#947342", 900: "#6E5531" },
        ink: { DEFAULT: "#1A1A2E", 50: "#E8E8F0", 100: "#C4C4D8", 200: "#9D9DBE", 300: "#7777A4", 400: "#50508A", 500: "#1A1A2E", 600: "#151525", 700: "#10101C", 800: "#0B0B13", 900: "#06060A" },
      },
      fontFamily: { display: ["Playfair Display", "Georgia", "serif"], body: ["Inter", "system-ui", "sans-serif"] },
      animation: { "fade-in": "fadeIn 0.6s ease-out", "slide-up": "slideUp 0.6s ease-out" },
      keyframes: { fadeIn: { "0%": { opacity: "0" }, "100%": { opacity: "1" } }, slideUp: { "0%": { opacity: "0", transform: "translateY(20px)" }, "100%": { opacity: "1", transform: "translateY(0)" } } },
    },
  },
  plugins: [],
};
