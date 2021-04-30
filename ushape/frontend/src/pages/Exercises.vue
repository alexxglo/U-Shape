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
      <q-tab v-for="part in exercises" :key="part"
      :name="part.exName" :label="part.exLabel"/>
      </q-tabs>
      <q-separator />
      <q-tab-panels v-model="tab" animated>
      <q-tab-panel v-for="(part, index) in exercises" :key="part"
          :name="exercises[index].exName">
          <ExerciseDraft :myKey="index"/>
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
      exercises: [
        {
          exName: 'chest',
          exLabel: 'Chest'
        },
        {
          exName: 'arms',
          exLabel: 'Arms'
        },
        {
          exName: 'back',
          exLabel: 'Back'
        },
        {
          exName: 'shoulders',
          exLabel: 'Shoulders'
        },
        {
          exName: 'legs',
          exLabel: 'Legs'
        }
      ],
      tab: 'chest'
    }
  }
}
</script>
