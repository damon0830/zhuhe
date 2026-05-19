// API 基础配置
const API_BASE = "/api"

interface FetchOptions {
  params?: Record<string, string>
}

export function useApi() {
  const config = useRuntimeConfig()

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
