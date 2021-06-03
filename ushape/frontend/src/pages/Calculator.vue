<template>
  <div class="q-pa-md">
    <q-table
      title="Calorie calculator"
      :data="data"
      :columns="columns"
      row-key="name"
      selection="multiple"
      :selected.sync="selected"
      :filter="filter"
      grid
      hide-header
      :rows-per-page-options="[8,16,24, 32, 40, 100]"
    >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

      <template v-slot:item="props">
        <div
          class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3 grid-style-transition"
          :style="props.selected ? 'transform: scale(0.95);' : ''"
        >
          <q-card :class="props.selected ? 'bg-grey-2' : ''">
            <q-card-section>
              <q-checkbox dense v-model="props.selected" :label="props.row.name" />
            </q-card-section>
            <q-separator />
            <q-list dense>
              <q-item v-for="col in props.cols.filter(col => col.name !== 'desc')" :key="col.name">
                <q-item-section>
                  <q-item-label>{{ col.label }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-item-label caption>{{ col.value }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card>
        </div>
      </template>
    </q-table>
    <div class="q-pa-md">
    <q-table
      title="Meals selected"
      :data="data"
      :columns="columns"
      row-key="name"
      selection="multiple"
      :selected.sync="selected"
      grid
      hide-header
      :filter="filter"
      :hide-pagination="true"
      :hide-selected-banner="true"
      :rows-per-page-options="[1000]"
    >
    <template v-slot:item="props">
         <q-card class="my-card q-ma-md justify-center items-center" :props = "props" v-if="props.selected == 1" style="max-width:250px; min-width:250px;">
           <div v-if ="props.row.calories > 300">
           <q-btn no-caps color="warning" text-color="dark" @click ="triggerCustomRegisteredType1(props.row.alternative, props.row.calories)" label="Healthier alternative" />
           </div>
      <q-card-section >
        <div class="text-h6">{{props.row.name}}</div>
        <div class="text-subtitle2">{{props.row.calories}} calories / 100g</div>
      </q-card-section>
      <q-separator />
      <q-card-actions vertical>
        <q-btn class="q-mt-sm" color="primary" unelevated @click="sum(props.row.calories)" label="Add"></q-btn>
        <q-btn color="black" unelevated @click="difference(props.row.calories), props.selected=0">Delete</q-btn>
      </q-card-actions>
    </q-card>
        </template>
        </q-table>
        <q-item class="bg-primary" rounded>
        <q-item-section >
          <q-item-label class="text-white q-mt-md">Your total calories: {{total_calories}}</q-item-label>
          <q-btn class="bg-white q-mt-md" style="max-width:100px" @click="reset()"> Reset </q-btn>
        </q-item-section>
      </q-item>
  </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      filter: '',
      total_calories: 0,
      selected: [],
      columns: [
        {
          name: 'desc',
          required: true,
          label: 'Dessert (100g serving)',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'calories', align: 'center', label: 'Calories', field: 'calories', sortable: true },
        { name: 'fat', label: 'Fat (g)', field: 'fat', sortable: true },
        { name: 'carbs', label: 'Carbs (g)', field: 'carbs' },
        { name: 'protein', label: 'Protein (g)', field: 'protein' },
        { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
        { name: 'calcium', label: 'Calcium (%)', field: 'calcium', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
        { name: 'iron', label: 'Iron (%)', field: 'iron', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
        { name: 'alternative' },
        { name: 'altkcal' }
      ],
      data: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          sodium: 87,
          calcium: '14%',
          iron: '1%',
          alternative: 'something',
          altkcal: '80'
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          sodium: 129,
          calcium: '8%',
          iron: '1%',
          alternative: 'something else',
          altkcal: '99'
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          sodium: 337,
          calcium: '6%',
          iron: '7%',
          alternative: 'something something',
          altkcal: '50'
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          sodium: 413,
          calcium: '3%',
          iron: '8%',
          alternative: 'something1',
          altkcal: '130'
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          sodium: 327,
          calcium: '7%',
          iron: '16%',
          alternative: 'something33',
          altkcal: '211'
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          sodium: 50,
          calcium: '0%',
          iron: '0%',
          alternative: 'something332',
          altkcal: '265'
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          sodium: 38,
          calcium: '0%',
          iron: '2%',
          alternative: 'something not lolli',
          altkcal: '190'
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          sodium: 562,
          calcium: '0%',
          iron: '45%',
          alternative: 'soo',
          altkcal: '302'
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          sodium: 326,
          calcium: '2%',
          iron: '22%',
          alternative: 'non donut',
          altkcal: '212'
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          sodium: 54,
          calcium: '12%',
          iron: '6%',
          alternative: 'non kitkat',
          altkcal: '332'
        }
      ]
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
    triggerCustomRegisteredType1 (alternative, kcal) {
      var finalMessage = 'A healthier alternative to this meal would be ' + alternative + ' with only ' + kcal + 'kcal per 100g!'
      this.$q.notify({
        type: 'my-notif',
        message: finalMessage
      })
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

<style lang="sass">
.grid-style-transition
  transition: transform .28s, background-color .28s
</style>
