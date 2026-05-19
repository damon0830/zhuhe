<template>
  <footer class="bg-navy text-cream-100">
    <div class="max-w-7xl mx-auto px-6 py-16">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-10">
        <!-- Brand -->
        <div class="md:col-span-2">
          <h3 class="font-display text-2xl text-cream-50 tracking-[0.3em] uppercase mb-4">ZhuHe</h3>
          <p class="text-cream-200 text-sm max-w-md leading-relaxed">
            Discover the timeless elegance of our curated pearl collection.
            Each piece tells a story of tradition, craftsmanship, and beauty.
          </p>
        </div>

        <!-- Links -->
        <div>
          <h4 class="font-display text-sm tracking-widest uppercase text-cream-50 mb-4">Explore</h4>
          <div class="flex flex-col gap-2 text-sm text-cream-200">
            <NuxtLink to="/collections" class="hover:text-cream-50 transition-colors">Collections</NuxtLink>
            <NuxtLink to="/products" class="hover:text-cream-50 transition-colors">Products</NuxtLink>
            <NuxtLink to="/about" class="hover:text-cream-50 transition-colors">Our Story</NuxtLink>
            <NuxtLink to="/journal" class="hover:text-cream-50 transition-colors">Journal</NuxtLink>
          </div>
        </div>

        <div>
          <h4 class="font-display text-sm tracking-widest uppercase text-cream-50 mb-4">Connect</h4>
          <div class="flex flex-col gap-2 text-sm text-cream-200">
            <a href="#" class="hover:text-cream-50 transition-colors">Instagram</a>
            <a href="#" class="hover:text-cream-50 transition-colors">WeChat</a>
            <a href="#" class="hover:text-cream-50 transition-colors">Contact</a>
            <a href="#" class="hover:text-cream-50 transition-colors">FAQ</a>
          </div>
        </div>
      </div>

      <div class="border-t border-navy-600 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-navy-300">
        <p>© 2026 ZhuHe. All rights reserved.</p>
        <div class="flex gap-6">
          <a href="#" class="hover:text-cream-50 transition-colors">Privacy Policy</a>
          <a href="#" class="hover:text-cream-50 transition-colors">Terms of Service</a>
          <a href="#" class="hover:text-cream-50 transition-colors">Shipping</a>
        </div>
      </div>
    </div>
  </footer>
</template>
