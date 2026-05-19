<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-screen flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-navy via-navy-500 to-ink">
        <div class="absolute inset-0 pearl-overlay"></div>
      </div>
      <div class="absolute top-1/4 left-1/4 w-64 h-64 rounded-full bg-lake-500/10 blur-3xl"></div>
      <div class="absolute bottom-1/4 right-1/4 w-96 h-96 rounded-full bg-lavender-500/10 blur-3xl"></div>

      <div class="relative text-center px-6 max-w-4xl">
        <p class="text-cream-200 tracking-[0.4em] uppercase text-sm mb-6 animate-fade-in">
          Pearls of Distinction
        </p>
        <h1 class="font-display text-5xl md:text-7xl text-cream-50 mb-8 leading-tight animate-slide-up">
          Timeless <span class="text-lake-300">Elegance</span><br />From the East
        </h1>
        <p class="text-cream-200 text-lg mb-10 max-w-2xl mx-auto animate-fade-in">
          Discover our curated collection of authentic pearl jewelry,
          where centuries of tradition meet contemporary design.
        </p>
        <div class="flex gap-4 justify-center animate-fade-in">
          <NuxtLink to="/collections" class="bg-cream-50 text-navy px-10 py-4 font-display font-medium
            hover:bg-cream-100 transition-all duration-300 tracking-wider uppercase text-sm">
            Explore Collections
          </NuxtLink>
          <NuxtLink to="/about" class="border-2 border-cream-200 text-cream-100 px-10 py-4 font-display font-medium
            hover:bg-cream-50 hover:text-navy transition-all duration-300 tracking-wider uppercase text-sm">
            Our Story
          </NuxtLink>
        </div>
      </div>

      <div class="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <svg class="w-6 h-6 text-cream-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </section>

    <!-- Value Propositions -->
    <section class="py-24 px-6">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <p class="section-subtitle">Why ZhuHe</p>
          <h2 class="section-title">The Pearl Essence</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
          <div v-for="item in values" :key="item.title" class="text-center group">
            <div class="w-16 h-16 mx-auto mb-6 rounded-full bg-lake-100 flex items-center justify-center
                        group-hover:bg-lake-200 transition-colors duration-300">
              <span class="text-2xl">{{ item.icon }}</span>
            </div>
            <h3 class="font-display text-xl text-navy mb-3">{{ item.title }}</h3>
            <p class="text-ink-300 text-sm leading-relaxed">{{ item.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Products -->
    <section class="py-24 bg-cream-100 px-6">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <p class="section-subtitle">Featured Selection</p>
          <h2 class="section-title">Our Finest Pearls</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="product in featuredProducts" :key="product.slug"
               class="group cursor-pointer" @click="navigateTo(`/products/${product.slug}`)">
            <div class="relative h-80 mb-4 bg-gradient-to-br from-navy-100 to-lavender-100 overflow-hidden">
              <div class="absolute inset-0 bg-navy/10 group-hover:bg-navy/20 transition-all duration-500"></div>
              <div class="absolute top-3 right-3 z-10 flex gap-2">
                <span v-if="product.is_new"
                  class="bg-lake text-navy text-xs px-3 py-1 font-medium tracking-wider uppercase">New</span>
                <span v-if="product.is_featured"
                  class="bg-navy text-cream-50 text-xs px-3 py-1 font-medium tracking-wider uppercase">Featured</span>
              </div>
              <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-navy/60 to-transparent">
                <p class="text-cream-200 text-xs tracking-widest uppercase mb-1">{{ product.pearl_type_display }}</p>
                <h3 class="font-display text-lg text-cream-50">{{ product.name }}</h3>
                <p class="text-lake-200 font-display text-sm mt-2">
                  {{ product.is_price_from ? 'From' : '' }} ¥{{ product.base_price.toLocaleString() }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Collections -->
    <section class="py-24 px-6" v-if="featuredCollections.length">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <p class="section-subtitle">Curated Selection</p>
          <h2 class="section-title">Featured Collections</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <NuxtLink v-for="col in featuredCollections" :key="col.slug" :to="`/collections/${col.slug}`"
            class="relative h-96 overflow-hidden group">
            <div class="absolute inset-0 bg-navy/40 group-hover:bg-navy/50 transition-colors duration-500 z-10"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-navy/80 via-transparent to-transparent z-20"></div>
            <div class="absolute bottom-0 left-0 right-0 p-8 z-30">
              <h3 class="font-display text-2xl text-cream-50 mb-2">{{ col.name }}</h3>
              <p class="text-cream-200 text-sm">{{ col.subtitle }}</p>
            </div>
            <div class="absolute inset-0 bg-gradient-to-br" :class="col.bg_gradient || 'from-lavender-300 to-lavender-500'"></div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Newsletter -->
    <section class="py-24 px-6">
      <div class="max-w-2xl mx-auto text-center">
        <p class="section-subtitle">Stay Inspired</p>
        <h2 class="section-title">Join Our Circle</h2>
        <p class="text-ink-300 mb-8">Be the first to know about new collections, exclusive events, and pearl care insights.</p>
        <form class="flex gap-4" @submit.prevent>
          <input type="email" placeholder="Your email address"
            class="flex-1 px-6 py-4 border-2 border-cream-200 bg-transparent
                   focus:border-navy focus:outline-none transition-colors
                   text-navy placeholder:text-ink-200" />
          <button type="submit" class="btn-primary whitespace-nowrap">Subscribe</button>
        </form>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const { featured, listCollections } = useProducts()

const values = [
  { icon: '🦪', title: 'Authentic Origins', desc: 'Every pearl is hand-selected from the finest waters, ensuring unparalleled quality and luster.' },
  { icon: '✨', title: 'Artisan Craftsmanship', desc: 'Our master jewelers combine traditional techniques with contemporary design for timeless pieces.' },
  { icon: '🌿', title: 'Sustainable Luxury', desc: 'Committed to ethical sourcing and environmentally responsible practices across our supply chain.' },
]

const featuredProducts = ref<Product[]>([])
const featuredCollections = ref<Collection[]>([])

onMounted(async () => {
  try {
    featuredProducts.value = await featured()
  } catch (e) {
    console.warn("Could not fetch featured products — backend may be offline")
  }
  try {
    featuredCollections.value = await listCollections(true)
  } catch (e) {
    console.warn("Could not fetch collections — backend may be offline")
  }
})
</script>
