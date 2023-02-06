<template>
  <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
    <a class="block relative h-48 rounded overflow-hidden">
      <img :alt="product.name" class="object-cover object-center w-full h-full block"
           :src="img">
    </a>
    <div class="mt-4">
      <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">{{product.category}}</h3>
      <h2 class="text-gray-900 title-font text-lg font-medium">{{product.name}}</h2>
      <p class="mt-1">{{product.price}}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  product: {
    type: Object,
    required: false
  },
})


</script>
