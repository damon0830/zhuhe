<template>
  <div class="pt-32 pb-24 px-6">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <p class="section-subtitle">Curated Selection</p>
        <h1 class="section-title">All Collections</h1>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div v-for="col in collections" :key="col.title" class="group cursor-pointer">
          <div class="relative h-80 mb-4 overflow-hidden bg-gradient-to-br" :class="col.bg">
            <div class="absolute inset-0 bg-navy/20 group-hover:bg-navy/30 transition-colors duration-500"></div>
          </div>
          <h3 class="font-display text-lg text-navy mb-1">{{ col.title }}</h3>
          <p class="text-ink-300 text-xs tracking-widest uppercase">{{ col.count }} pieces</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const collections = [
  { title: 'Akoya Classics', count: 24, bg: 'from-lavender-200 to-lavender-400' },
  { title: 'South Sea Treasures', count: 18, bg: 'from-sandy-200 to-sandy-400' },
  { title: 'Freshwater Essence', count: 32, bg: 'from-lake-200 to-lake-400' },
  { title: 'Tahitian Noir', count: 14, bg: 'from-ink-400 to-ink-600' },
  { title: 'Golden South Sea', count: 10, bg: 'from-cream-300 to-sandy-300' },
  { title: 'Baroque & Unique', count: 27, bg: 'from-lavender-300 to-lake-200' },
]
</script>
