import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import { auth } from './auth.module'
import * as VueGoogleMaps from 'vue2-google-maps'
// import example from './module-example'

Vue.use(Vuex)
Vue.use(axios)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCbBtlQS2qgCS11AHHG3Uakb9D1r6w8ixg',
    region: 'RO',
    language: 'en',
    libraries: 'places' // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)
    // If you want to set the version, you can do so:
    // v: '3.26',
  }
  // If you intend to programmatically custom event listener code
  // (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  // instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  // you might need to turn this on.
  // autobindAllEvents: false,
  // If you want to manually install components, e.g.
  // import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  // Vue.component('GmapMarker', GmapMarker)
  // then disable the following:
  // installComponents: true,
})
/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */
const store = new Vuex.Store({
  modules: {
    auth
  }
})

export default store
