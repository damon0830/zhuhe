export interface CartItem {
  id: number
  variant: {
    id: number
    sku: string
    name: string
    price: number
    stock: number
    image: string | null
  }
  quantity: number
  subtotal: number
}

export interface Cart {
  id: number
  items: CartItem[]
  total_items: number
  total_price: number
}

export function useCart() {
  const cart = useState<Cart | null>("cart", () => null)

  async function fetchCart(): Promise<Cart> {
    const data = await $fetch<Cart>("/api/cart/", {
      headers: getAuthHeaders(),
    })
    cart.value = data
    return data
  }

  async function addToCart(variantId: number, quantity: number = 1) {
    const item = await $fetch("/api/cart/add/", {
      method: "POST",
      body: { variant_id: variantId, quantity },
      headers: getAuthHeaders(),
    })
    await fetchCart()
    return item
  }

  async function updateQuantity(itemId: number, quantity: number) {
    const data = await $fetch(`/api/cart/items/${itemId}/`, {
      method: "PATCH",
      body: { quantity },
      headers: getAuthHeaders(),
    })
    await fetchCart()
    return data
  }

  async function removeItem(itemId: number) {
    await $fetch(`/api/cart/items/${itemId}/remove/`, {
      method: "DELETE",
      headers: getAuthHeaders(),
    })
    await fetchCart()
  }

  async function clearCart() {
    await $fetch("/api/cart/clear/", {
      method: "DELETE",
      headers: getAuthHeaders(),
    })
    cart.value = { id: 0, items: [], total_items: 0, total_price: 0 }
  }

  return { cart, fetchCart, addToCart, updateQuantity, removeItem, clearCart }
}

function getAuthHeaders(): Record<string, string> {
  if (process.client) {
    const stored = localStorage.getItem("zhuhe_tokens")
    if (stored) {
      const tokens = JSON.parse(stored)
      return { Authorization: `Bearer ${tokens.access}` }
    }
  }
  return {}
}
