// API 基础配置
interface FetchOptions {
  params?: Record<string, string>
}

export function useApi() {
  const config = useRuntimeConfig()
  const API_BASE = config.public.apiBase || "/api"

  async function fetchJSON<T>(endpoint: string, options: FetchOptions = {}): Promise<T> {
    const params = new URLSearchParams(options.params || {})
    const qs = params.toString() ? `?${params.toString()}` : ""
    const url = `${API_BASE}${endpoint}${qs}`
    const { data, error } = await useFetch<T>(url)
    if (error.value) {
      console.error(`API Error: ${url}`, error.value)
      throw error.value
    }
    return data.value as T
  }

  return { fetchJSON }
}
