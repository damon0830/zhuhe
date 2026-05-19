<template>
  <div class="pt-32 pb-24 px-6 min-h-screen flex items-start justify-center">
    <div class="w-full max-w-md">
      <div class="text-center mb-10">
        <p class="section-subtitle">Join Us</p>
        <h1 class="section-title">Create Account</h1>
      </div>

      <form @submit.prevent="handleRegister" class="space-y-6">
        <div>
          <label class="block text-xs tracking-widest uppercase text-ink-300 mb-2">Username</label>
          <input v-model="username" type="text" required
            class="w-full px-6 py-4 border-2 border-cream-200 bg-transparent
                   focus:border-navy focus:outline-none transition-colors text-navy" />
        </div>
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
          {{ loading ? 'Creating...' : 'Create Account' }}
        </button>

        <p class="text-center text-ink-300 text-sm">
          Already have an account?
          <NuxtLink to="/auth/login" class="text-navy underline">Sign In</NuxtLink>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
const { register } = useAuth()
const router = useRouter()

const username = ref("")
const email = ref("")
const password = ref("")
const error = ref("")
const loading = ref(false)

async function handleRegister() {
  error.value = ""
  loading.value = true
  try {
    await register(email.value, username.value, password.value)
    router.push("/")
  } catch (e: any) {
    if (e?.data && typeof e.data === "object") {
      error.value = Object.values(e.data).flat().join(", ")
    } else {
      error.value = "Registration failed"
    }
  } finally {
    loading.value = false
  }
}
</script>
