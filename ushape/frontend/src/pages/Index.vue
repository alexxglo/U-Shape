<template>
  <div class="q-pa-md q-gutter-md">
    <div class="row justify-between">

    <q-parallax
      src="~assets/fitness_parallax.png"
    >
      <h1 class="text-bold text-white">U-SHAPE</h1>
    </q-parallax>
    <q-card class="my-card">
    <q-card-section>
    <h3 class="text-weight-medium">What is U-Shape? </h3>
    <h5> U-Shape is a new fitness application that helps you achieve your goals in new ways. <br>
    Do you want to lose weight? Do you want to gain muscle? U-Shape is a great path to start you fitness journey. </h5>
    <q-parallax class="dimmed"
      src="~assets/fitness_parallax2.png"
    >
    </q-parallax>
       <h3 class="text-weight-medium">Why U-Shape? </h3>
       <h5> U-Shape is a new fitness application that helps you achieve your goals in new ways. <br>
    Do you want to lose weight? Do you want to gain muscle? U-Shape is a great path to start you fitness journey. </h5>
<q-list bordered>
      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-icon color="primary" name="dashboard" />
        </q-item-section>

        <h6 class="text-weight-light">Count your daily intake through our accesible calorie calculator</h6>
      </q-item>

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar color="primary" text-color="white" icon="photo" />
        </q-item-section>

        <h6 class="text-weight-light">Easy to track your progress through uploaded photos of yourself</h6>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar color="primary" text-color="white" icon="local_pizza" />
        </q-item-section>

        <h6 class="text-weight-light">Suggested diets with different meal options</h6>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar color="primary" text-color="white" icon="emoji_events" />
        </q-item-section>

        <h6 class="text-weight-light">Useful exercises to help you achieve your goals</h6>
      </q-item>
      </q-list>
      </q-card-section>
    </q-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageIndex'
}
</script>
<style lang="sass" scoped>
.my-card
  width: 100%
</style>
