<template>
  <div class="pt-32 pb-24 px-6 min-h-screen">
    <div class="max-w-4xl mx-auto">
      <div class="mb-12">
        <p class="section-subtitle">My Account</p>
        <h1 class="section-title">Order History</h1>
      </div>

      <div v-if="!orders.length" class="text-center py-20">
        <p class="text-ink-300 mb-6">No orders yet</p>
        <NuxtLink to="/products" class="btn-primary">Start Shopping</NuxtLink>
      </div>

      <div v-else class="space-y-4">
        <NuxtLink v-for="order in orders" :key="order.id" :to="`/orders/${order.id}`"
          class="block p-6 bg-cream-100 hover:bg-cream-200 transition-colors">
          <div class="flex justify-between items-start">
            <div>
              <p class="font-display text-navy text-lg">{{ order.order_number }}</p>
              <p class="text-ink-300 text-xs">{{ new Date(order.created_at).toLocaleDateString() }}</p>
            </div>
            <div class="text-right">
              <p class="font-display text-navy">¥{{ order.total.toLocaleString() }}</p>
              <p class="text-xs" :class="statusColor(order.status)">{{ statusLabel(order.status) }}</p>
            </div>
          </div>
          <p class="text-ink-300 text-xs mt-2">{{ order.items_count }} item(s)</p>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { list } = useOrders()
const orders = ref<Order[]>([])

function statusLabel(s: string) {
  const labels: Record<string, string> = {
    pending: "Pending", confirmed: "Confirmed", processing: "Processing",
    shipped: "Shipped", delivered: "Delivered", cancelled: "Cancelled", refunded: "Refunded",
  }
  return labels[s] || s
}

function statusColor(s: string) {
  const colors: Record<string, string> = {
    pending: "text-yellow-600", confirmed: "text-blue-600", processing: "text-blue-600",
    shipped: "text-purple-600", delivered: "text-green-600", cancelled: "text-red-400", refunded: "text-red-400",
  }
  return colors[s] || "text-ink-300"
}

onMounted(async () => {
  try { orders.value = await list() } catch {}
})
</script>
