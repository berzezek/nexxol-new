<template>
  <MainAside
    :categories="categories"
  />
</template>

<script setup>

import { useCategoryStore } from '@/stores/category'

const catalogStore = useCategoryStore()
catalogStore.getCategories();
const categories = computed(() => catalogStore.categories)

</script>

<style scoped>

</style>
