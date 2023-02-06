import {defineStore} from "pinia";
import {IProduct} from "@/types";
import {BASE_API_URL} from "@/utils/constants"

export const useProductStore = defineStore({
  id: "product",
  state: () => ({
    products: [] as IProduct[],
    product: {} as IProduct,
    pendingProducts: false,
    pendingProduct: false,
  }),
  getters: {},
  actions: {
    getProducts: async function () {
      this.pendingProducts = true;
      try {
        const {data: products, error, execute, refresh, pending} = await useLazyFetch(`${BASE_API_URL}products/`);
        if (!error.value && !pending.value) {
          this.products = products.value as IProduct[];
          this.pendingProducts = false;
        }
      } catch (error) {
        console.log(error);
      }
    },
    getProduct: async function (id: Number | String) {
      this.pendingProduct = true;
      try {
        const {data: product, error, execute, refresh, pending} = await useLazyFetch(`${BASE_API_URL}products/${id}/`);
        if (!error.value && !pending.value) {
          this.product = product.value as IProduct;
          this.pendingProduct = false;
        }
      } catch (error) {
        console.log(error);
      }
    },

  },


});
