export interface User {
  id: number
  email: string
  username: string
  phone: string
  avatar: string | null
  preferred_language: string
  date_joined: string
}

export interface AuthTokens {
  access: string
  refresh: string
}

export function useAuth() {
  const { fetchJSON } = useApi()
  const user = useState<User | null>("auth-user", () => null)
  const tokens = useState<AuthTokens | null>("auth-tokens", () => null)

  // Hydrate from localStorage on init
  if (process.client && !tokens.value) {
    const stored = localStorage.getItem("zhuhe_tokens")
    const storedUser = localStorage.getItem("zhuhe_user")
    if (stored) tokens.value = JSON.parse(stored)
    if (storedUser) user.value = JSON.parse(storedUser)
  }

  function saveTokens(t: AuthTokens, u: User) {
    tokens.value = t
    user.value = u
    if (process.client) {
      localStorage.setItem("zhuhe_tokens", JSON.stringify(t))
      localStorage.setItem("zhuhe_user", JSON.stringify(u))
    }
  }

  function clearAuth() {
    tokens.value = null
    user.value = null
    if (process.client) {
      localStorage.removeItem("zhuhe_tokens")
      localStorage.removeItem("zhuhe_user")
    }
  }

  async function register(email: string, username: string, password: string) {
    const res = await $fetch("/api/accounts/register/", {
      method: "POST",
      body: { email, username, password, password2: password },
    }) as any
    saveTokens({ access: res.access, refresh: res.refresh }, res.user)
    return res.user as User
  }

  async function login(email: string, password: string) {
    const res = await $fetch("/api/accounts/login/", {
      method: "POST",
      body: { email, password },
    }) as any
    saveTokens({ access: res.access, refresh: res.refresh }, res.user)
    return res.user as User
  }

  async function logout() {
    clearAuth()
    navigateTo("/")
  }

  function isLoggedIn() {
    return !!user.value
  }

  return { user, tokens, register, login, logout, isLoggedIn }
}
