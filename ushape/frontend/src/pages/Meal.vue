<template>
    <q-card class="my-card q-ma-md justify-center items-center" v-if="props.selected == 1" style="max-width:250px; min-width:250px;">
           <div v-if ="props.row.calories > 300">
           <q-btn no-caps color="warning" text-color="dark" @click ="healthierAlternative(props.row.alternative, props.row.altkcal)" label="Healthier alternative?" />
            <q-btn icon="close" size="xs" color="red" @click="progress = false, difference(props.row.calories), props.selected=0" class="float-right on-right" dense/>
           </div>
           <div v-else>
               <q-btn no-caps color="positive" text-color="dark" label="Good choice!" />
               <q-btn icon="close" size="xs" color="red" @click="progress = false, difference(props.row.calories), props.selected=0" class="float-right on-right" dense/>
           </div>
      <q-card-section >
        <div class="text-h6">{{props.row.name}}</div>
        <div class="text-subtitle2">{{props.row.calories}} calories / 100g</div>
        <div class ="text-h6 q-my-md"><q-btn icon="remove" size="sm" round dense @click="portion--"/>
         {{ portion }}
        <q-btn icon="add" size="sm" round dense @click="portion++"/></div>
        <div class="text-subtitle2">You have selected {{ portion*100 }} grams </div>
      </q-card-section>
      <q-separator />
      <q-card-actions vertical>
        <q-btn :loading="progress" color="primary" @click="progress = true, sum(props.row.calories), emitToParent()">
      Add meal
      <template v-slot:loading>
        <q-spinner-hearts class="on-left" />
        Added!
      </template>
    </q-btn>
      </q-card-actions>
    </q-card>
</template>
<script>
export default {
  props: ['props'],
  data () {
    return {
      total_calories: 0,
      portion: 0,
      quantity: 100,
      progress: false
    }
  },
  methods: {
    sum (add) {
      this.total_calories = this.total_calories + add
      return this.total_calories
    },
    difference (diff) {
      if (this.total_calories - diff >= 0) {
        this.total_calories = this.total_calories - diff
      }
      return this.total_calories
    },
    reset () {
      this.total_calories = 0
      return this.total_calories
    },
    healthierAlternative (alternative, kcal) {
      var finalMessage = 'A healthier alternative to this meal would be ' + alternative + ' with only ' + kcal + 'kcal per 100g!'
      this.$q.notify({
        type: 'my-notif',
        message: finalMessage
      })
    },
    emitToParent (event) {
      this.$emit('childToParent', this.props.row.calories * this.portion)
    }
  },

  created () {
    this.$q.notify.registerType('my-notif', {
      icon: 'announcement',
      progress: true,
      color: 'warning',
      textColor: 'dark'
    })
  }
}
</script>
