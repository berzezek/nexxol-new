<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-wrap -m-4">
        <ProductCard
            v-for="product in products"
            :key="product.id"
            :product="product"
            @click="$router.push(`/products/${product.id}`)"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import {useProductStore} from '@/stores/product';

const productStore = useProductStore();
productStore.getProducts();
const products = computed(() => productStore.products);

</script>

<style scoped>

</style>
