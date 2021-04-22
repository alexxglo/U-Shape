<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn align="left" class="full-width" color="primary" >
    <q-item-section
      v-if="icon"
      avatar
    >
      <q-icon :name="icon" />
    </q-item-section>

    <q-item-section>
    <router-link :to= "'/' + routename" style="text-decoration: none; color: inherit;">
      <q-item-label>{{ title }}</q-item-label>
      </router-link>
    </q-item-section>
    </q-btn>
    </div>
</template>

<script>
export default {
  name: 'EssentialLink',
  props: {
    title: {
      type: String,
      required: true
    },

    component: {
      type: String,
      default: '#'
    },

    icon: {
      type: String,
      default: ''
    },
    routename: {
      type: String,
      default: ''
    }
  }
}
</script>
