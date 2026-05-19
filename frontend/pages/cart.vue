<template>
  <div class="pt-32 pb-24 px-6 min-h-screen">
    <div class="max-w-4xl mx-auto">
      <div class="flex justify-between items-center mb-12">
        <div>
          <p class="section-subtitle">Your Cart</p>
          <h1 class="section-title">Shopping Cart</h1>
        </div>
        <button v-if="cart?.items?.length" @click="handleClear" class="btn-ghost text-sm">
          Clear All
        </button>
      </div>

      <!-- Empty cart -->
      <div v-if="!cart?.items?.length" class="text-center py-20">
        <p class="text-ink-300 mb-6">Your cart is empty</p>
        <NuxtLink to="/products" class="btn-primary">Browse Products</NuxtLink>
      </div>

      <!-- Cart items -->
      <div v-else class="space-y-6">
        <div v-for="item in cart.items" :key="item.id"
             class="flex items-center gap-6 p-6 bg-cream-100">
          <!-- Placeholder image -->
          <div class="w-24 h-24 bg-gradient-to-br from-navy-100 to-lavender-100 flex-shrink-0"></div>

          <!-- Info -->
          <div class="flex-1">
            <h3 class="font-display text-navy">{{ item.variant.name }}</h3>
            <p class="text-ink-300 text-xs">{{ item.variant.sku }}</p>
            <p class="font-display text-navy mt-2">¥{{ item.variant.price.toLocaleString() }}</p>
          </div>

          <!-- Quantity -->
          <div class="flex items-center gap-3">
            <button @click="updateQty(item.id, item.quantity - 1)"
              class="w-8 h-8 border border-cream-200 flex items-center justify-center text-navy hover:border-navy transition-colors">−</button>
            <span class="w-8 text-center text-navy font-medium">{{ item.quantity }}</span>
            <button @click="updateQty(item.id, item.quantity + 1)"
              class="w-8 h-8 border border-cream-200 flex items-center justify-center text-navy hover:border-navy transition-colors">+</button>
          </div>

          <!-- Subtotal -->
          <div class="text-right w-24">
            <p class="font-display text-navy">¥{{ item.subtotal.toLocaleString() }}</p>
            <button @click="removeItem(item.id)" class="text-ink-300 text-xs hover:text-red-400 transition-colors mt-1">
              Remove
            </button>
          </div>
        </div>

        <!-- Summary -->
        <div class="border-t border-cream-200 pt-8 flex flex-col items-end gap-4">
          <div class="text-right">
            <p class="text-ink-300 text-sm">Total ({{ cart.total_items }} items)</p>
            <p class="font-display text-3xl text-navy">¥{{ cart.total_price.toLocaleString() }}</p>
          </div>
          <button class="btn-primary">Proceed to Checkout</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { cart, fetchCart, updateQuantity, removeItem, clearCart } = useCart()
const { isLoggedIn } = useAuth()

onMounted(async () => {
  if (isLoggedIn()) {
    try { await fetchCart() } catch {}
  }
})

async function updateQty(itemId: number, qty: number) {
  if (qty <= 0) {
    await removeItem(itemId)
  } else {
    await updateQuantity(itemId, qty)
  }
}

async function handleClear() {
  await clearCart()
}
</script>
