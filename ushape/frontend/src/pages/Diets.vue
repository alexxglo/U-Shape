<template>
  <div>
    <q-splitter
      v-model="splitterModel"
      >

      <template v-slot:before>
        <q-tabs
          v-model="tab"
          vertical
          class="text-blue-6"
        >
        <q-tab v-for="(item, index) in items" :key="item"
        :name="items[index].dietName" :icon="items[index].icon"
        :label="items[index].label">
        </q-tab>
        </q-tabs>
      </template>

      <template v-slot:after>
        <q-tab-panels
          v-model="tab"
          animated
          swipeable
          vertical
          transition-prev="jump-up"
          transition-next="jump-up"
        >
          <q-tab-panel v-for="(item, index) in items" :key="item"
          :name="items[index].dietName">
          <Diet1 :componentNo="index"/>
          </q-tab-panel>
        </q-tab-panels>
      </template>

    </q-splitter>
  </div>
</template>

<script>
import Diet1 from './Diet1.vue'
export default {
  components: { Diet1 },
  data () {
    return {
      items: [
        {
          dietName: 'diet 1',
          icon: 'fastfood',
          label: 'Diet 1'
        },
        {
          dietName: 'diet 2',
          icon: 'local_dining',
          label: 'Diet 2'
        },
        {
          dietName: 'diet 3',
          icon: 'fitness_center',
          label: 'Diet 3'
        }
      ],
      tab: 'diet 1',
      splitterModel: 15,
      myKey: 0
    }
  }
}
</script>
