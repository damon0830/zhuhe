<template>
  <div class="pt-32 pb-24 px-6 min-h-screen">
    <div class="max-w-3xl mx-auto text-center">
      <div class="w-16 h-16 mx-auto mb-6 rounded-full bg-lake-100 flex items-center justify-center">
        <span class="text-3xl">✅</span>
      </div>
      <p class="section-subtitle">Order Confirmed</p>
      <h1 class="section-title">Thank You!</h1>

      <div v-if="order" class="mt-10 bg-cream-100 p-8 text-left">
        <div class="flex justify-between items-center mb-6">
          <div>
            <p class="text-ink-300 text-xs tracking-widest uppercase">Order Number</p>
            <p class="font-display text-xl text-navy">{{ order.order_number }}</p>
          </div>
          <span class="px-4 py-2 text-xs tracking-wider uppercase font-medium bg-lake text-navy rounded">
            {{ statusLabel(order.status) }}
          </span>
        </div>

        <div class="space-y-3 mb-6">
          <div v-for="item in order.items" :key="item.id"
            class="flex justify-between text-sm py-2 border-b border-cream-200 last:border-0">
            <span class="text-ink-300">{{ item.product_name }} — {{ item.variant_name }} x{{ item.quantity }}</span>
            <span class="text-navy">¥{{ item.subtotal.toLocaleString() }}</span>
          </div>
        </div>

        <div class="border-t border-cream-200 pt-4 space-y-1 text-sm">
          <div class="flex justify-between"><span class="text-ink-300">Subtotal</span><span class="text-navy">¥{{ order.subtotal.toLocaleString() }}</span></div>
          <div class="flex justify-between"><span class="text-ink-300">Shipping</span><span class="text-navy">{{ order.shipping_cost ? '¥'+order.shipping_cost : 'Free' }}</span></div>
          <div class="flex justify-between"><span class="text-ink-300">VAT</span><span class="text-navy">¥{{ order.tax.toLocaleString() }}</span></div>
          <div class="flex justify-between font-display text-lg border-t border-cream-200 pt-2 mt-2">
            <span class="text-navy">Total</span><span class="text-navy">¥{{ order.total.toLocaleString() }}</span>
          </div>
        </div>

        <div v-if="order.shipping_address?.recipient_name" class="border-t border-cream-200 mt-6 pt-6 text-sm">
          <p class="text-ink-300 text-xs tracking-widest uppercase mb-2">Shipping To</p>
          <p class="text-navy">{{ order.shipping_address.recipient_name }}</p>
          <p class="text-ink-300">{{ order.shipping_address.address_line1 }}{{ order.shipping_address.address_line2 ? ', ' + order.shipping_address.address_line2 : '' }}</p>
          <p class="text-ink-300">{{ order.shipping_address.city }}, {{ order.shipping_address.country }} {{ order.shipping_address.postal_code }}</p>
        </div>
      </div>

      <div class="mt-10 flex gap-4 justify-center">
        <NuxtLink to="/orders" class="btn-outline">View All Orders</NuxtLink>
        <NuxtLink to="/products" class="btn-primary">Continue Shopping</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const { get } = useOrders()

const order = ref<OrderDetail | null>(null)

function statusLabel(s: string) {
  const labels: Record<string, string> = {
    pending: "Pending Payment", confirmed: "Confirmed", processing: "Processing",
    shipped: "Shipped", delivered: "Delivered", cancelled: "Cancelled", refunded: "Refunded",
  }
  return labels[s] || s
}

onMounted(async () => {
  const id = parseInt(route.params.id as string)
  if (id) {
    try { order.value = await get(id) } catch {}
  }
})
</script>
