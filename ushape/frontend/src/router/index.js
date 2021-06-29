import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'
import store from './../store/index'
import { sync } from 'vuex-router-sync'
import VueCompositionAPI from '@vue/composition-api'
Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

Vue.router = new VueRouter({
  scrollBehavior: () => ({ x: 0, y: 0 }),
  routes,
  // Leave these as they are and change in quasar.conf.js instead!
  // quasar.conf.js -> build -> vueRouterMode
  // quasar.conf.js -> build -> publicPath
  mode: process.env.VUE_ROUTER_MODE,
  base: process.env.VUE_ROUTER_BASE,
  beforeEach: (to, from, next) => {
    const publicPages = ['/login', '/register', '/diets']
    const authRequired = !publicPages.includes(to.path)
    const loggedIn = localStorage.getItem('user')
    // trying to access a restricted page + not logged in
    // redirect to login page
    if (authRequired && !loggedIn) {
      next({ name: '/login' })
    } else {
      next()
    }
  }
}
)

// Sync Vuex and vue-router;
sync(store, Vue.router)

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
Vue.use(VueCompositionAPI)
Vue.axios.defaults.baseURL = '/api'
export default Vue.router
