<template>
  <div v-if="product" class="pt-32 pb-24 px-6">
    <div class="max-w-7xl mx-auto">
      <!-- Breadcrumb -->
      <NuxtLink to="/products" class="text-ink-300 text-xs tracking-widest uppercase hover:text-navy transition-colors mb-8 inline-block">
        ← Back to Products
      </NuxtLink>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
        <!-- Gallery -->
        <div>
          <div class="aspect-square bg-gradient-to-br from-navy-100 to-lavender-100 relative overflow-hidden mb-4">
            <div class="absolute top-3 left-3 z-10 flex gap-2">
              <span v-if="product.is_new"
                class="bg-lake text-navy text-xs px-3 py-1 font-medium tracking-wider uppercase">New</span>
            </div>
            <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-navy/40 to-transparent">
              <p class="text-cream-200 text-xs tracking-widest uppercase">{{ product.pearl_type_display }}</p>
            </div>
          </div>
        </div>

        <!-- Product Info -->
        <div>
          <p class="section-subtitle mb-2">{{ product.category }}</p>
          <h1 class="font-display text-3xl md:text-4xl text-navy mb-4">{{ product.name }}</h1>

          <!-- Price -->
          <div class="flex items-baseline gap-3 mb-8">
            <span class="font-display text-3xl text-navy">
              ¥{{ selectedVariant ? selectedVariant.price.toLocaleString() : product.base_price.toLocaleString() }}
            </span>
            <span v-if="selectedVariant?.compare_at_price" class="text-ink-300 line-through text-sm">
              ¥{{ selectedVariant.compare_at_price.toLocaleString() }}
            </span>
            <span v-if="product.is_price_from && !selectedVariant" class="text-ink-300 text-sm">starting from</span>
          </div>

          <!-- Variant selector -->
          <div v-if="product.variants.length > 1" class="mb-8">
            <p class="text-xs tracking-widest uppercase text-ink-300 mb-3">Select Option</p>
            <div class="flex flex-wrap gap-3">
              <button v-for="v in product.variants" :key="v.id"
                @click="selectVariant(v)"
                class="px-6 py-3 text-sm border transition-all duration-300"
                :class="selectedVariant?.id === v.id
                  ? 'bg-navy text-cream-50 border-navy'
                  : 'border-cream-200 text-ink-300 hover:border-navy hover:text-navy'">
                {{ v.name }}
                <span v-if="v.stock < 3 && v.stock > 0" class="text-xs opacity-60 ml-2">Only {{ v.stock }} left</span>
                <span v-if="v.stock === 0" class="text-xs text-red-400 ml-2">Sold out</span>
              </button>
            </div>
          </div>

          <!-- Add to cart -->
          <button class="btn-primary w-full mb-8"
            :disabled="selectedVariant?.stock === 0"
            :class="{ 'opacity-50 cursor-not-allowed': selectedVariant?.stock === 0 }">
            {{ selectedVariant?.stock === 0 ? 'Sold Out' : 'Add to Cart' }}
          </button>

          <!-- Specs -->
          <div class="border-t border-cream-200 pt-8">
            <h3 class="font-display text-lg text-navy mb-4">Pearl Specifications</h3>
            <dl class="grid grid-cols-2 gap-y-4 gap-x-8 text-sm">
              <div v-for="spec in specs" :key="spec.label" class="flex justify-between">
                <dt class="text-ink-300">{{ spec.label }}</dt>
                <dd class="text-navy font-medium">{{ spec.value }}</dd>
              </div>
            </dl>
          </div>

          <!-- Description -->
          <div class="border-t border-cream-200 mt-8 pt-8">
            <div class="text-ink-300 text-sm leading-relaxed whitespace-pre-line">{{ product.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Loading -->
  <div v-else class="pt-40 text-center text-ink-200">
    <p>Loading...</p>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const { getBySlug } = useProducts()

const product = ref<ProductDetail | null>(null)
const selectedVariant = ref<ProductVariant | null>(null)

function selectVariant(v: ProductVariant) {
  selectedVariant.value = v
}

const specs = computed(() => {
  const p = product.value
  if (!p) return []
  return [
    { label: "Type", value: p.pearl_type_display },
    { label: "Size", value: p.pearl_size },
    { label: "Shape", value: p.pearl_shape },
    { label: "Color", value: p.pearl_color },
    { label: "Luster", value: p.pearl_luster },
    { label: "Quality", value: p.pearl_quality },
    { label: "Material", value: p.material },
  ].filter(s => s.value)
})

onMounted(async () => {
  const slug = route.params.slug as string
  try {
    product.value = await getBySlug(slug)
    const defaultVariant = product.value.variants.find(v => v.is_default) || product.value.variants[0]
    if (defaultVariant) {
      selectedVariant.value = defaultVariant
    }
  } catch (e) {
    console.error("Failed to load product", e)
  }
})
</script>
