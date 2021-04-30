<template>
  <div class="q-pa-md">
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
      ]
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
