export interface Order {
  id: number
  order_number: string
  status: string
  total: number
  currency: string
  items_count: number
  created_at: string
  paid_at: string | null
}

export interface OrderDetail extends Order {
  user: number
  email: string
  shipping_address: Record<string, any>
  billing_address: Record<string, any>
  subtotal: number
  shipping_cost: number
  tax: number
  items: OrderItem[]
  notes: string
  updated_at: string
}

export interface OrderItem {
  id: number
  product_name: string
  variant_name: string
  sku: string
  price: number
  quantity: number
  subtotal: number
}

export function useOrders() {
  async function list(): Promise<Order[]> {
    return $fetch("/api/orders/", { headers: getHeaders() })
  }

  async function get(id: number): Promise<OrderDetail> {
    return $fetch(`/api/orders/${id}/`, { headers: getHeaders() })
  }

  async function create(data: { shipping_address_id?: number; shipping_address?: any; notes?: string }): Promise<OrderDetail> {
    return $fetch("/api/orders/create/", {
      method: "POST",
      body: data,
      headers: getHeaders(),
    })
  }

  async function cancel(id: number): Promise<OrderDetail> {
    return $fetch(`/api/orders/${id}/cancel/`, {
      method: "POST",
      headers: getHeaders(),
    })
  }

  return { list, get, create, cancel }
}

function getHeaders() {
  if (process.client) {
    const stored = localStorage.getItem("zhuhe_tokens")
    if (stored) {
      const tokens = JSON.parse(stored)
      return { Authorization: `Bearer ${tokens.access}` }
    }
  }
  return {}
}
