<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md full-width">
      <q-card>
        <q-tabs
        v-model="tab"
        inline-label
        outside-arrows
        mobile-arrows
        class="bg-primary text-white shadow-2"
      >
        <q-tab name="grains" icon="mail" label="Grains" />
        <q-tab name="vegetables" icon="alarm" label="Vegetables" />
        <q-tab name="fruits" icon="movie" label="Fruits" />
        <q-tab name="dairy" icon="photo" label="Dairy" />
        <q-tab name="meat" icon="slow_motion_video" label="Meat" />
        <q-tab name="nuts" icon="people" label="Nuts" />
      </q-tabs>

        <q-separator />

        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="grains">
            <div class="text-h6">Grains</div>
            <div class="q-pa-md">
    <div v-if="isLoaded">
    <q-table
    class="my-sticky-column-table"
      :columns="columns_grains"
      :data="data_grains"
      row-key="name"
      @row-click="onRowClick">
    </q-table>
    </div>
  </div>
          </q-tab-panel>

          <q-tab-panel name="vegetables">
            <div class="text-h6">Vegetables</div>
            <div class="q-pa-md">
    <div v-if="isLoaded">
    <q-table
    class="my-sticky-column-table"
      :columns="columns_grains"
      :data="data_vegetables"
      row-key="name"
      @row-click="onRowClick">
    </q-table>
    </div>
  </div>
          </q-tab-panel>
          <q-tab-panel name="fruits">
            <div class="text-h6">Fruits</div>
           <div class="q-pa-md">
    <div v-if="isLoaded">
    <q-table
    class="my-sticky-column-table"
      :columns="columns_grains"
      :data="data_fruits"
      row-key="name"
      @row-click="onRowClick">
    </q-table>
    </div>
  </div>
          </q-tab-panel>
          <q-tab-panel name="dairy">
            <div class="text-h6">Dairy</div>
            <div class="q-pa-md">
    <div v-if="isLoaded">
    <q-table
    class="my-sticky-column-table"
      :columns="columns_grains"
      :data="data_dairy"
      row-key="name"
      @row-click="onRowClick">
    </q-table>
    </div>
  </div>
          </q-tab-panel>

          <q-tab-panel name="meat">
            <div class="text-h6">Meat</div>
            <div class="q-pa-md">
    <div v-if="isLoaded">
    <q-table
    class="my-sticky-column-table"
      :columns="columns_grains"
      :data="data_meat"
      row-key="name"
      @row-click="onRowClick">
    </q-table>
    </div>
  </div>
          </q-tab-panel>

          <q-tab-panel name="nuts">
            <div class="text-h6">Nuts</div>
            <div class="q-pa-md">
    <div v-if="isLoaded">
    <q-table
    class="my-sticky-column-table"
      :columns="columns_grains"
      :data="data_nuts"
      row-key="name"
      @row-click="onRowClick">
    </q-table>
    </div>
  </div>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
        <q-separator />
    </div>
  </div>
</template>

<script>
//  import axios from 'axios'
import { api } from 'boot/axios'
export default {
  name: 'CalorieCalculator',
  data () {
    return {
      tab: 'grains',
      data: [],
      data_grains: [],
      data_vegetables: [],
      data_fruits: [],
      data_dairy: [],
      data_meat: [],
      data_nuts: [],
      returnData: [],
      newProduct: '',
      key: 'id',
      isLoaded: false,
      columns_grain: [
        {
          name: 'name',
          required: true,
          label: 'Grains (100g serving)',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true,
          classes: 'bg-grey-2 ellipsis',
          style: 'max-width: 100px',
          headerClasses: 'bg-primary text-white'
        },
        { name: 'calories', align: 'center', label: 'Calories', field: 'calories', sortable: true },
        { name: 'fat', label: 'Fat (g)', field: 'fat', sortable: true },
        { name: 'carbs', label: 'Carbs (g)', field: 'carbs' },
        { name: 'protein', label: 'Protein (g)', field: 'protein' },
        { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
        { name: 'calcium', label: 'Calcium (%)', field: 'calcium', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
        { name: 'iron', label: 'Iron (%)', field: 'iron', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) }
      ]
    }
  },
  methods: {
    getData: function (data, keyword) {
      this.returnData = []
      this.returnData = data.filter(obj => {
        return obj.isType === keyword
      })
      for (var i = 0, len = this.returnData.length; i < len; i++) {
        delete this.returnData[i].isType
      }
      return this.returnData
    },
    loadData: function () {
      api.get('/api/calorie-list/')
        .then((response) => {
          this.data = response.data
          this.isLoaded = true
          for (var i = 0, len = this.data.length; i < len; i++) {
            delete this.data[i].id
          }
          this.data_grains = this.getData(this.data, 'grains')
          this.data_vegetables = this.getData(this.data, 'vegetables')
          this.data_fruits = this.getData(this.data, 'fruits')
          this.data_dairy = this.getData(this.data, 'dairy')
          this.data_meat = this.getData(this.data, 'meat')
          this.data_nuts = this.getData(this.data, 'nuts')
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
    },
    editRow (props) {
      this.noti()
      // do something
      this.noti = this.$q.notify({
        type: 'info',
        textColor: 'grey-10',
        multiLine: true,
        message: `I'll edit row data => ${JSON.stringify(props.row).split(',').join(', ')}`,
        timeout: 2000
      })
    }
  },
  mounted () {
    this.loadData()
  }
}
</script>
<style lang="sass">
.my-sticky-column-table
  /* am schimbat max-width ca sa apara tabela pe toata pagina
    might cause issues later on
     */
  max-width: 1920px
  thead tr:first-child th:first-child
    /* bg color is important for th; just specify one */
    background-color: #fff
  td:first-child
    background-color: #f5f5dc
  th:first-child,
  td:first-child
    position: sticky
    left: 0
    z-index: 1
</style>
