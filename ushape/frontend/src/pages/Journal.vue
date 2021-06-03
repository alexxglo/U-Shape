<template>
  <div class="q-pa-md">
    <div v-if="!isLoggedIn">
      <q-dialog v-model="carousel" persistent>
      <q-carousel
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        v-model="slide"
        control-color="primary"
        navigation-icon="radio_button_unchecked"
        navigation
        padding
        height="300px"
        class="bg-white shadow-1 rounded-borders"
      >
        <q-carousel-slide :name="1" class="column no-wrap flex-center">
          <q-icon name="style" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            This feature is called the Journal, an important component of our app that we take pride in. Because of this, we kindly ask for you to login or register to U-Shape.
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="2" class="column no-wrap flex-center">
          <q-icon name="live_tv" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            The journal tracks your progress as you advance in your fitness journey. Upload your images everyday and you'll see your hard work results in no time!
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap flex-center q-mt-lg">
          <q-icon name="layers" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            Register and start your journey! If you already have an account, please log in.
          </div>
          <q-card-actions align="center">
            <q-btn to="/login" label="LOGIN" outline color="primary" class = "q-mr-lg"/>
            <q-btn to="/register" label="REGISTER" outline color="primary" class = "q-xml-lg"/>
        </q-card-actions>
        </q-carousel-slide>
      </q-carousel>
    </q-dialog>
    </div>

    <div v-else>
    <div>
    <q-btn
      push
      color="primary"
      label="Upload"
      icon="file_upload"
      class="q-mb-md float-right"/>
    <h4 class="text-weight-bold"> Your journey </h4>
    </div>
    <div class="q-gutter-md row items-start">
    <q-img
        v-for="image in gallery"
        :key="image"
        :src="image"
        :ratio="1"
        basic
        spinner-color="white"
        class="rounded-borders my-gallery"
      >
        <div class="absolute-bottom text-center text-italic text-body2">
          None
        </div>
      </q-img>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
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
      return this.$store.auth.user.username
    }
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
