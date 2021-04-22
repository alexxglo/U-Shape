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
          <q-tab name="diet 1"  icon="local_dining" label="Diet 1" />
          <q-tab name="diet 2" icon="fastfood" label="Diet 2" />
          <q-tab name="diet 3" icon="fitness_center" label="Diet 3" />
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
          <q-tab-panel name="diet 1">
            <Diet1/>
           </q-tab-panel>

          <q-tab-panel name="diet 2">
            <div class="text-h4 q-mb-md">Diet 2</div>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
          </q-tab-panel>

          <q-tab-panel name="diet 3">
            <div class="text-h4 q-mb-md">Diet 3</div>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
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
      tab: 'diet 1',
      splitterModel: 10
    }
  }
}
</script>
