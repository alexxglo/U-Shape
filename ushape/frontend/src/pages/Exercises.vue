<template>
<div class="q-pa-md">
    <div class="q-gutter-y-md full-width">
      <q-tabs
        v-model="tab"
        no-caps
        outside-arrows
        mobile-arrows
        class="bg-primary text-white shadow-2"
      >
        <q-tab name="chest" label="Chest" />
        <q-tab name="arms" label="Arms" />
        <q-tab name="back" label="Back" />
        <q-tab name="shoulders" label="Shoulders" />
        <q-tab name="legs" label="Legs" />
      </q-tabs>
      <q-separator />
      <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="chest">
        <ExerciseDraft/>
      </q-tab-panel>
      <q-tab-panel name="arms">
        <h5>hello</h5>
      </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>
import ExerciseDraft from './ExerciseDraft'
export default {
  components: { ExerciseDraft },
  data () {
    return {
      tab: 'chest'
    }
  }
}
</script>
