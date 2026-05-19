export default defineNuxtConfig({
  compatibilityDate: "2026-05-01",
  ssr: true,
  app: {
    head: { title: "ZhuHe", meta: [{ name: "description", content: "ZhuHe -- Pearls of Distinction" }] }
  },
  modules: ["@nuxtjs/tailwindcss", "@nuxt/image"],
  css: ["~/assets/css/main.css"],
  nitro: {
    preset: "node-server",
    devProxy: { "/api": { target: "http://localhost:8000/api", changeOrigin: true } }
  },
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || "/api"
    }
  }
})
