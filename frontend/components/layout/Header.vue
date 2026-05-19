<template>
  <header class="fixed top-0 left-0 right-0 z-50 bg-cream-50/95 backdrop-blur-sm">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex justify-between items-center h-10 text-xs text-ink-300 border-b border-cream-200">
        <span>Pearls of Distinction</span>
        <div class="flex gap-6">
          <NuxtLink to="/auth/login" v-if="!user" class="hover:text-navy transition-colors">Sign In</NuxtLink>
          <button v-else @click="handleLogout" class="hover:text-navy transition-colors">Sign Out</button>
          <NuxtLink to="/cart" class="hover:text-navy transition-colors">
            Cart <span v-if="cartTotal">({{ cartTotal }})</span>
          </NuxtLink>
        </div>
      </div>

      <nav class="flex justify-between items-center h-20">
        <NuxtLink to="/" class="font-display text-2xl text-navy tracking-[0.3em] uppercase">ZhuHe</NuxtLink>
        <div class="hidden md:flex gap-10">
          <NuxtLink to="/collections" class="nav-link">Collections</NuxtLink>
          <NuxtLink to="/products" class="nav-link">Products</NuxtLink>
          <NuxtLink to="/about" class="nav-link">Our Story</NuxtLink>
        </div>
        <button class="md:hidden text-navy" @click="mobileOpen = !mobileOpen">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              :d="mobileOpen ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16'" />
          </svg>
        </button>
      </nav>
    </div>

    <div v-if="mobileOpen" class="md:hidden bg-cream-50 border-t border-cream-200">
      <div class="px-6 py-4 flex flex-col gap-4 text-navy">
        <NuxtLink to="/collections" @click="mobileOpen = false">Collections</NuxtLink>
        <NuxtLink to="/products" @click="mobileOpen = false">Products</NuxtLink>
        <NuxtLink to="/about" @click="mobileOpen = false">Our Story</NuxtLink>
        <NuxtLink to="/cart" @click="mobileOpen = false">Cart</NuxtLink>
        <NuxtLink v-if="!user" to="/auth/login" @click="mobileOpen = false">Sign In</NuxtLink>
        <button v-else @click="handleLogout" class="text-left">Sign Out</button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
const { user, logout } = useAuth()
const { cart, fetchCart } = useCart()

const mobileOpen = ref(false)
const cartTotal = computed(() => cart.value?.total_items || 0)

async function handleLogout() {
  mobileOpen.value = false
  await logout()
}

onMounted(async () => {
  if (user.value) {
    try { await fetchCart() } catch {}
  }
})
</script>

<style scoped>
.nav-link {
  @apply text-ink-300 text-sm tracking-widest uppercase font-body
         hover:text-navy transition-colors duration-300;
}
.nav-link.router-link-exact-active {
  @apply text-navy;
}
</style>
