<template>
  <div class="q-pa-md">
    <h4> Greetings, {{getUsername}}! </h4>
    <div v-if="!isLoggedIn">
      <PopupInfo/>
    </div>

    <div v-else>
    <div>
      <q-file color="black" class="float-right" style="max-width:300px" outlined v-model="modelPhoto" label="Upload image">
        <template v-slot:prepend>
          <q-icon name="attachment" />
        </template>
        <template v-slot:append>
          <q-icon name="close" @click.stop="modelPhoto = null" class="cursor-pointer" />
        </template>
        <template v-slot:after>
          <q-btn round dense flat icon="send" @click="uploadData()" />
        </template>
      </q-file>
    <h4 class="text-weight-bold"> Your journey </h4>
    </div>
    <div class="q-gutter-md row items-start">
    <q-img
        v-for="img in photoData"
        :key="img"
        :src="img"
        :ratio="1"
        basic
        spinner-color="white"
        class="rounded-borders my-gallery"
      >
      <div v-if="indivDelete">
      <q-btn icon="delete" size="sm" @click="confirm=true" text-color="red" color="white" class="float-right q-mr-xs q-mt-xs" dense>
      <q-tooltip content-class="bg-red">Delete this picture</q-tooltip>
      </q-btn>
      <q-dialog v-model="confirm" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="red" text-color="white" />
          <span class="q-ml-sm">Are you sure you want to delete this picture?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn flat label="Yes" color="primary" @click="deleteData(img)" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog></div>
      </q-img>
    </div>
  </div>
  </div>
</template>

<script>
import { api } from 'boot/axios'
import PopupInfo from './PopupInfo'
export default {
  components: { PopupInfo },
  data () {
    return {
      photoData: [],
      allData: [],
      confirm: false,
      indivDelete: false,
      modelPhoto: null,
      file: '',
      gallery: [
        'ushapelogo.png',
        'ushapelogo.png',
        'fitness_parallax.jpg',
        'fitness_parallax.jpg'
      ],
      carousel: true,
      slide: 1,
      lorem: 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Natus, ratione eum minus fuga, quasi dicta facilis corporis magnam, suscipit at quo nostrum!'
    }
  },
  computed: {
    testRouteName () {
      // functie care ma ajuta sa vad pe ce pagina sunt
      var path = this.$router.currentRoute.path
      if (path === '/login' || path === '/register') {
        return false
      } else {
        return true
      }
    },
    isLoggedIn () {
      return this.$store.state.auth.status.loggedIn
    },
    getUsername () { // functie ce returneaza username
      return this.$store.state.auth.usernameName
    },
    check () {
      console.log(this.modelPhoto.name)
      return this.modelPhoto
    }
  },
  methods: {
    getData: function (data, keyword) {
      this.returnData = []
      this.finalData = []
      this.returnData = data.filter(obj => {
        return obj.username === keyword
      })
      for (var i = 0, len = this.returnData.length; i < len; i++) {
        this.finalData.push(this.returnData[i].image)
        this.allData.push(this.returnData[i])
      }
      return this.finalData
    },
    loadData: function () {
      api.get('/api/imageupload/')
        .then((response) => {
          this.data = response.data
          this.isLoaded = true
          this.photoData = this.getData(this.data, this.getUsername)
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
    uploadData: function () {
      const formData = new FormData()
      formData.append('username', this.getUsername)
      formData.append('image', this.modelPhoto)
      console.log(formData)
      api.post('/api/imageupload/', formData)
        .then((response) => {
          this.$router.push('/img-check').catch(() => {})
        }
        )
        .catch(error => {
          this.errorMessage = error.message
          console.error('There was an error broder!', error)
        })
    },
    deleteData (itemDel) {
      console.log('O sa dau delete la: ')
      console.log(itemDel, 1)
      for (var i = 0, len = this.allData.length; i < len; i++) {
        if (this.allData[i].image === itemDel) {
          this.pkDel = this.allData[i].id
        }
      }
      console.log('Id-ul de sters:', this.pkDel)
      api.delete('/api/imageupload/', itemDel, this.pkDel)
    }
  },
  mounted () {
    this.loadData()
  }
}
</script>
<style lang="sass">
.my-gallery
    @media (min-width: 701px)
      width:31%
    @media (max-width: 700px)
      width: 45%
    @media (max-width: 335px)
      width: 100%
</style>
