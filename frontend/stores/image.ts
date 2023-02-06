import {defineStore} from "pinia";
import {IImage} from "@/types";
import {BASE_API_URL} from "@/utils/constants"

export const useImageStore = defineStore({
  id: "image",
  state: () => ({
    images: [] as IImage[],
    pendingImages: true,
  }),
  getters: {},
  actions: {
    getImages: async function (product_id: Number | String) {
      this.pendingImages = true;
      try {
        const {data: images, error, execute, refresh, pending} = await useLazyFetch(`${BASE_API_URL}images/?product=${product_id}`);
        if (!error.value && !pending.value) {
          this.images = images.value as IImage[];
          this.pendingImages = false;
        }
      } catch (error) {
        console.log(error);
      }
    },

  }
});
