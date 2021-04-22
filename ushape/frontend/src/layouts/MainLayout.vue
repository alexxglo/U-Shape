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
        Log in
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
    component: 'caloriecalculator',
    routename: 'calorie-calculator'
  },
  {
    title: 'Journal',
    icon: 'book',
    component: 'journal',
    routename: 'journal'
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
  }
}
</script>
