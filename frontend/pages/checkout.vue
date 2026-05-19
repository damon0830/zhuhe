<template>
  <div class="pt-32 pb-24 px-6 min-h-screen">
    <div class="max-w-4xl mx-auto">
      <div class="mb-12">
        <p class="section-subtitle">Checkout</p>
        <h1 class="section-title">Complete Your Order</h1>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="text-center py-20 text-ink-200">Loading...</div>

      <!-- Empty cart -->
      <div v-else-if="!cart?.items?.length" class="text-center py-20">
        <p class="text-ink-300 mb-6">Your cart is empty</p>
        <NuxtLink to="/products" class="btn-primary">Browse Products</NuxtLink>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-5 gap-12">
        <!-- Left: form -->
        <div class="md:col-span-3">
          <h3 class="font-display text-lg text-navy mb-6">Shipping Address</h3>

          <div v-if="addresses.length" class="mb-6 space-y-3">
            <label v-for="addr in addresses" :key="addr.id"
              class="flex items-start gap-3 p-4 border-2 cursor-pointer transition-colors"
              :class="selectedAddr === addr.id ? 'border-navy bg-navy-50' : 'border-cream-200 hover:border-navy'">
              <input type="radio" :value="addr.id" v-model="selectedAddr" class="mt-1 accent-navy" />
              <div class="text-sm">
                <p class="font-medium text-navy">{{ addr.recipient_name }}</p>
                <p class="text-ink-300">{{ addr.address_line1 }}, {{ addr.city }}, {{ addr.country }} {{ addr.postal_code }}</p>
                <p class="text-ink-300">{{ addr.phone }}</p>
              </div>
            </label>
          </div>

          <p v-if="error" class="text-red-400 text-sm mb-4">{{ error }}</p>

          <button @click="handleSubmit"
            :disabled="submitting"
            class="btn-primary w-full"
            :class="{ 'opacity-50': submitting }">
            {{ submitting ? 'Processing...' : `Pay ¥${(cart.total_price + shippingCost + tax).toLocaleString()}` }}
          </button>
        </div>

        <!-- Right: summary -->
        <div class="md:col-span-2">
          <h3 class="font-display text-lg text-navy mb-6">Order Summary</h3>
          <div class="space-y-3 mb-6">
            <div v-for="item in cart.items" :key="item.id" class="flex justify-between text-sm">
              <span class="text-ink-300">{{ item.variant.name }} x{{ item.quantity }}</span>
              <span class="text-navy">¥{{ (item.variant.price * item.quantity).toLocaleString() }}</span>
            </div>
          </div>

          <div class="border-t border-cream-200 pt-4 space-y-2 text-sm">
            <div class="flex justify-between">
              <span class="text-ink-300">Subtotal</span>
              <span class="text-navy">¥{{ cart.total_price.toLocaleString() }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-ink-300">Shipping</span>
              <span class="text-navy">{{ shippingCost === 0 ? 'Free' : `¥${shippingCost}` }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-ink-300">VAT (20%)</span>
              <span class="text-navy">¥{{ tax.toLocaleString() }}</span>
            </div>
            <div class="flex justify-between border-t border-cream-200 pt-2 font-display text-lg">
              <span class="text-navy">Total</span>
              <span class="text-navy">¥{{ (cart.total_price + shippingCost + tax).toLocaleString() }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { cart, fetchCart } = useCart()
const { create } = useOrders()
const router = useRouter()
const { fetchJSON } = useApi()

const addresses = ref<any[]>([])
const selectedAddr = ref<number | null>(null)
const error = ref("")
const loading = ref(true)
const submitting = ref(false)

const shippingCost = computed(() => (cart.value?.total_price || 0) >= 200 ? 0 : 15)
const tax = computed(() => Math.round((cart.value?.total_price || 0) * 0.20))

onMounted(async () => {
  try {
    await fetchCart()
    const data = await $fetch<any[]>("/api/accounts/addresses/", {
      headers: getAuthHeadersLocal(),
    })
    addresses.value = data
    if (data.length) selectedAddr.value = data[0].id
  } catch (e) {
    console.warn("Checkout init failed", e)
  } finally {
    loading.value = false
  }
})

async function handleSubmit() {
  if (!cart.value?.items?.length) return
  error.value = ""
  submitting.value = true
  try {
    const order = await create({
      shipping_address_id: selectedAddr.value || undefined,
    })
    router.push(`/orders/${order.id}`)
  } catch (e: any) {
    error.value = e?.data?.detail || e?.data?.message || "Order failed"
  } finally {
    submitting.value = false
  }
}

function getAuthHeadersLocal() {
  if (process.client) {
    const stored = localStorage.getItem("zhuhe_tokens")
    if (stored) return { Authorization: `Bearer ${JSON.parse(stored).access}` }
  }
  return {}
}
</script>
