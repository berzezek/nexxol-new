import {defineStore} from "pinia";
import {ICategory} from "@/types";
import {BASE_API_URL} from "@/utils/constants"


export const useCategoryStore = defineStore({
  id: "category",
  state: () => ({
    categories: [] as ICategory[],
    pendingCategories: false,
  }),
  getters: {},
  actions: {
    getCategories: async function () {
      this.pendingCategories = true;
      try {
        const {data: categories, error, execute, refresh, pending} = await useLazyFetch(`${BASE_API_URL}categories/`);
        if (!error.value && !pending.value) {
          this.categories = categories.value as ICategory[];
          this.pendingCategories = false;
        }
      } catch (e) {
        console.log(e);
      }
    }
  }
});
