<template>
  <div class="pt-32 pb-24 px-6 min-h-screen flex items-start justify-center">
    <div class="w-full max-w-md">
      <div class="text-center mb-10">
        <p class="section-subtitle">Welcome Back</p>
        <h1 class="section-title">Sign In</h1>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-xs tracking-widest uppercase text-ink-300 mb-2">Email</label>
          <input v-model="email" type="email" required
            class="w-full px-6 py-4 border-2 border-cream-200 bg-transparent
                   focus:border-navy focus:outline-none transition-colors text-navy" />
        </div>
        <div>
          <label class="block text-xs tracking-widest uppercase text-ink-300 mb-2">Password</label>
          <input v-model="password" type="password" required
            class="w-full px-6 py-4 border-2 border-cream-200 bg-transparent
                   focus:border-navy focus:outline-none transition-colors text-navy" />
        </div>

        <p v-if="error" class="text-red-400 text-sm">{{ error }}</p>

        <button type="submit" class="btn-primary w-full" :disabled="loading">
          {{ loading ? 'Signing in...' : 'Sign In' }}
        </button>

        <p class="text-center text-ink-300 text-sm">
          Don't have an account?
          <NuxtLink to="/auth/register" class="text-navy underline">Register</NuxtLink>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
const { login } = useAuth()
const router = useRouter()

const email = ref("")
const password = ref("")
const error = ref("")
const loading = ref(false)

async function handleLogin() {
  error.value = ""
  loading.value = true
  try {
    await login(email.value, password.value)
    router.push("/")
  } catch (e: any) {
    error.value = e?.data?.detail || "Login failed"
  } finally {
    loading.value = false
  }
}
</script>
