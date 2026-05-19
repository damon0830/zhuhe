export interface Product {
  id: number
  name: string
  slug: string
  short_description: string
  pearl_type: string
  pearl_type_display: string
  pearl_size: string
  pearl_color: string
  base_price: number
  is_price_from: boolean
  cover_image: string | null
  is_featured: boolean
  is_new: boolean
  category_name: string
  created_at: string
}

export interface ProductDetail extends Product {
  name_en: string
  description: string
  pearl_shape: string
  pearl_luster: string
  pearl_quality: string
  material: string
  category: string
  collections: string[]
  images: ProductImage[]
  variants: ProductVariant[]
  tags: string[]
  meta_title: string
  meta_description: string
}

export interface ProductImage {
  id: number
  image: string
  alt_text: string
  sort_order: number
  is_primary: boolean
}

export interface ProductVariant {
  id: number
  sku: string
  name: string
  chain_length: string
  pearl_size: string
  color_option: string
  price: number
  compare_at_price: number | null
  stock: number
  is_default: boolean
  image: string | null
  is_active: boolean
}

export interface Category {
  id: number
  name: string
  slug: string
  description: string
  image: string | null
  sort_order: number
  product_count: number
}

export interface Collection {
  id: number
  name: string
  slug: string
  description: string
  subtitle: string
  image: string | null
  bg_gradient: string
  is_featured: boolean
  product_count: number
}

export function useProducts() {
  const { fetchJSON } = useApi()

  function list(params?: Record<string, string>): Promise<Product[]> {
    return fetchJSON<Product[]>("/products/", { params })
  }

  function getBySlug(slug: string): Promise<ProductDetail> {
    return fetchJSON<ProductDetail>(`/products/${slug}/`)
  }

  function featured(): Promise<Product[]> {
    return list({ is_featured: "true" })
  }

  function newArrivals(): Promise<Product[]> {
    return list({ is_new: "true" })
  }

  function byCollection(slug: string): Promise<Product[]> {
    return list({ "collections__slug": slug })
  }

  function byCategory(slug: string): Promise<Product[]> {
    return list({ "category__slug": slug })
  }

  function listCategories(): Promise<Category[]> {
    return fetchJSON<Category[]>("/categories/")
  }

  function listCollections(featuredOnly?: boolean): Promise<Collection[]> {
    const params = featuredOnly ? { featured: "true" } : undefined
    return fetchJSON<Collection[]>("/collections/", { params })
  }

  return { list, getBySlug, featured, newArrivals, byCollection, byCategory, listCategories, listCollections }
}
