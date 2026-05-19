<template>
  <header class="fixed top-0 left-0 right-0 z-50 bg-cream-50/95 backdrop-blur-sm">
    <div class="max-w-7xl mx-auto px-6">
      <!-- Top bar -->
      <div class="flex justify-between items-center h-10 text-xs text-ink-300 border-b border-cream-200">
        <span>Pearls of Distinction</span>
        <div class="flex gap-6">
          <a href="#" class="hover:text-navy transition-colors">Search</a>
          <a href="#" class="hover:text-navy transition-colors">Account</a>
          <a href="#" class="hover:text-navy transition-colors">Cart (0)</a>
        </div>
      </div>

      <!-- Main nav -->
      <nav class="flex justify-between items-center h-20">
        <NuxtLink to="/" class="font-display text-2xl text-navy tracking-[0.3em] uppercase">
          ZhuHe
        </NuxtLink>

        <div class="hidden md:flex gap-10">
          <NuxtLink to="/collections" class="nav-link">Collections</NuxtLink>
          <NuxtLink to="/products" class="nav-link">Products</NuxtLink>
          <NuxtLink to="/about" class="nav-link">Our Story</NuxtLink>
          <NuxtLink to="/journal" class="nav-link">Journal</NuxtLink>
        </div>

        <!-- Mobile menu button -->
        <button class="md:hidden text-navy" @click="mobileOpen = !mobileOpen">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              :d="mobileOpen ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16'" />
          </svg>
        </button>
      </nav>
    </div>

    <!-- Mobile menu -->
    <div v-if="mobileOpen" class="md:hidden bg-cream-50 border-t border-cream-200">
      <div class="px-6 py-4 flex flex-col gap-4 text-navy">
        <NuxtLink to="/collections" @click="mobileOpen = false">Collections</NuxtLink>
        <NuxtLink to="/products" @click="mobileOpen = false">Products</NuxtLink>
        <NuxtLink to="/about" @click="mobileOpen = false">Our Story</NuxtLink>
        <NuxtLink to="/journal" @click="mobileOpen = false">Journal</NuxtLink>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
const mobileOpen = ref(false)
</script>

<style scoped>
.nav-link {
  @apply text-ink-300 text-sm tracking-widest uppercase font-body
         hover:text-navy transition-colors duration-300;
}
.nav-link.router-link-active {
  @apply text-navy;
}
</style>
