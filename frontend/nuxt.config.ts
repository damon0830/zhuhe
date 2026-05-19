export default defineNuxtConfig({
  compatibilityDate: "2026-05-01",
  app: {
    head: { title: "ZhuHe", meta: [{ name: "description", content: "ZhuHe -- Pearls of Distinction" }] }
  },
  modules: ["@nuxtjs/tailwindcss", "@nuxt/image"],
  css: ["~/assets/css/main.css"],
  nitro: { devProxy: { "/api": { target: "http://localhost:8000/api", changeOrigin: true } } },
})
