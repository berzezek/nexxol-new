import {setAbsoluteSqliteDatabaseUrlForPrisma} from './prisma/utils'

setAbsoluteSqliteDatabaseUrlForPrisma()

export default defineNuxtConfig({
  runtimeConfig: {
    version: '0.0.1'
  },
  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-svgo',
    '@huntersofbook/naive-ui-nuxt',
    '@pinia/nuxt',
  ],
  extends: ['@sidebase/core'],
  typescript: {
    shim: false
  },
  css: [
    '~/assets/css/input.css',
  ],

})
