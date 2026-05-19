<template>
  <div class="pt-32 pb-24 px-6">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <p class="section-subtitle">{{ category?.name || 'All Products' }}</p>
        <h1 class="section-title">Pearl Collection</h1>
      </div>

      <!-- Filter bar -->
      <div class="flex flex-wrap gap-4 mb-12 justify-center">
        <button v-for="cat in categories" :key="cat.slug"
          @click="currentCategory = cat.slug; loadProducts()"
          class="px-6 py-2 text-sm tracking-wider uppercase font-body transition-all duration-300"
          :class="currentCategory === cat.slug
            ? 'bg-navy text-cream-50'
            : 'text-ink-300 border border-cream-200 hover:border-navy hover:text-navy'">
          {{ cat.name }}
        </button>
      </div>

      <!-- Product grid -->
      <div v-if="products.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <div v-for="product in products" :key="product.slug"
             class="group cursor-pointer" @click="navigateTo(`/products/${product.slug}`)">
          <div class="relative h-72 mb-4 bg-gradient-to-br from-navy-100 to-lavender-100 overflow-hidden">
            <div class="absolute inset-0 bg-navy/10 group-hover:bg-navy/20 transition-all duration-500"></div>
            <div class="absolute top-3 right-3 z-10 flex gap-2">
              <span v-if="product.is_new"
                class="bg-lake text-navy text-xs px-3 py-1 font-medium tracking-wider uppercase">New</span>
            </div>
            <div class="absolute bottom-0 left-0 right-0 p-5 bg-gradient-to-t from-navy/60 to-transparent">
              <p class="text-cream-200 text-xs tracking-widest uppercase mb-1">{{ product.pearl_type_display }}</p>
              <h3 class="font-display text-base text-cream-50">{{ product.name }}</h3>
              <p class="text-lake-200 font-display text-sm mt-1">
                {{ product.is_price_from ? 'From' : '' }} ¥{{ product.base_price.toLocaleString() }}
              </p>
            </div>
          </div>
          <p class="text-ink-300 text-xs leading-relaxed line-clamp-2">{{ product.short_description }}</p>
        </div>
      </div>

      <!-- Loading / empty -->
      <div v-else class="text-center py-20 text-ink-200">
        <p v-if="loading">Loading...</p>
        <p v-else>No products found.</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { list, listCategories } = useProducts()

const products = ref<Product[]>([])
const categories = ref<Category[]>([])
const currentCategory = ref("")
const loading = ref(true)

async function loadProducts() {
  loading.value = true
  try {
    const params: Record<string, string> = {}
    if (currentCategory.value) {
      params["category__slug"] = currentCategory.value
    }
    products.value = await list(params)
  } catch (e) {
    console.warn("Failed to load products")
    products.value = []
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  try {
    categories.value = await listCategories()
  } catch (e) {
    console.warn("Failed to load categories")
  }
  await loadProducts()
})
</script>
