<template>
  <div>
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
          <q-icon name="layers" color="primary" size="56px" />
          <div class="q-mt-md text-center">
            The journal tracks your progress as you advance in your fitness journey. Upload your images everyday and you'll see your hard work results in no time!
          </div>
        </q-carousel-slide>
        <q-carousel-slide :name="3" class="column no-wrap flex-center q-mt-lg">
          <q-icon name="live_tv" color="primary" size="56px" />
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
</template>

<script>
export default {
  data () {
    return {
      carousel: true,
      slide: 1
    }
  }
}
</script>

<style>

</style>
