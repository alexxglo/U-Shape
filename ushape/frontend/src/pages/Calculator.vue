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
         <Meal :props="props" v-on:childToParent="onChildClick"/>
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
import Meal from './Meal.vue'
import { api } from 'boot/axios'
export default {
  components: { Meal },
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
        { name: 'protein', label: 'Protein (g)', field: 'protein' }
      ],
      data: []
    }
  },
  methods: {
    reset () {
      this.total_calories = 0
      this.selected.splice(0)
      return this.total_calories
    },
    onChildClick (value) {
      this.total_calories = this.total_calories + value
    },
    loadData: function () {
      api.get('/api/meal-list/')
        .then((response) => {
          this.data = response.data
          this.isLoaded = true
          for (var i = 0, len = this.data.length; i < len; i++) {
            delete this.data[i].id
          }
        }
        )
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem'
          })
        })
    }
  },
  mounted () {
    this.loadData()
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
