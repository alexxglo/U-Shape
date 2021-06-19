<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
        <router-link to="/" style="text-decoration: none; color: inherit;">
          U-Shape
        </router-link>
        </q-toolbar-title>
        <div v-if="!isLoggedIn && !testRouteName">
        <q-btn to="/login" label="LOGIN" outline color="white" class = "q-mr-md"/>
        <q-btn to="/register" label="REGISTER" outline color="white" class = ""/>
       </div>
        <div v-else>
         <q-btn @click.prevent="logOut"> Logout </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Menu
        </q-item-label>
        <EssentialLink
          v-for="component in essentialLinks"
          :key="component.title"
          v-bind="component"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Diets',
    icon: 'food_bank',
    component: 'diets',
    routename: 'diets'
  },
  {
    title: 'Exercises',
    icon: 'directions_run',
    component: 'exercises',
    routename: 'exercises'
  },
  {
    title: 'Calorie calculator',
    icon: 'calculate',
    component: 'nutritionaltables',
    routename: 'calorie-calculator'
  },
  {
    title: 'Journal',
    icon: 'book',
    component: 'journal',
    routename: 'journal'
  },
  {
    title: 'Nearby Gyms',
    icon: 'map',
    component: 'map',
    routename: 'map'
  },
  {
    title: 'Suggestions',
    icon: 'music_note',
    component: 'suggestions',
    routename: 'suggestions'
  },
  {
    title: 'Special fitness',
    icon: 'accessible_forward',
    component: 'specialfitness',
    routename: 'special-fitness'
  }

]

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  },
  computed: {
    isLoggedIn () {
      return this.$store.state.auth.status.loggedIn
    },
    getUsername () { // functie ce returneaza username
      return this.$store
    }
  },
  methods: {
    logOut () {
      this.$store.dispatch('auth/logout')
      this.$store.state.auth.usernameName = 'loggedOut'
      this.$router.push('/login')
    }
  }
}
</script>
