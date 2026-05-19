<template>
  <div>
    <LayoutHeader />
    <main class="min-h-screen">
      <NuxtPage />
    </main>
    <LayoutFooter />
  </div>
</template>

<script setup lang="ts">
useHead({
  bodyAttrs: {
    class: 'bg-cream-50'
  }
})
</script>
