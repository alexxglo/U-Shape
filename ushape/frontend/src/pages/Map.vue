<template>
  <div class="q-pa-md absolute-center items-start q-gutter-md my-map">
    <q-card flat>
      <div>
    <GmapMap class="my-map" :zoom="11" :center="{lat: this.latx, lng: this.laty}"
        ref="map">
      <GmapMarker v-for="(marker, index) in markers"
        :key="index"
        :position="marker.latLng"
        />
    </GmapMap>
  </div>

      <q-card-section class="my-desc">
        <div class="text-h5 text-center q-mt-sm q-mb-xs">Looking for a gym?</div>
        <div class="text-caption text-center text-black">
          U-Shape always provides the best recommandations for when you're looking for a muscle-building temple.
        </div>
        <div class="q-mt-xl absolute-center q-pt-lg q-pb-xl">
        <q-btn class="q-mr-md q-mt-xl" color="primary" icon="map" @click="generate">Show nearby gyms</q-btn>
        <q-btn-dropdown class="q-mt-xl" color="primary" icon="add" label="Choose your city">
          <q-list>
        <q-item clickable v-close-popup @click="onBucharestClick">
          <q-item-section>
            <q-item-label>Bucharest</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onClujClick">
          <q-item-section>
            <q-item-label>Cluj-Napoca</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="onIasiClick">
          <q-item-section>
            <q-item-label>Iasi</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
          </q-btn-dropdown></div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data () {
    return {
      expanded: false,
      markers: [],
      place: null,
      latx: 44.439,
      laty: 26.096
    }
  },
  methods: {
    generate () {
      const spread = Math.random() + 0.001

      this.center = {
        lat: this.latx,
        lng: this.laty
      }

      this.markers = _.range(30)
        .map(m => ({
          latLng: {
            lat: this.center.lat + (Math.random() - 0.4) * spread,
            lng: this.center.lng + (Math.random() - 0.4) * spread
          }
        }))
    },
    onBucharestClick () {
      this.latx = 44.439
      this.laty = 26.096
    },
    onClujClick () {
      this.latx = 46.770
      this.laty = 23.591
    },
    onIasiClick () {
      this.latx = 47.151
      this.laty = 27.587
    }
  }
}
</script>
<style scoped lang="sass">
.my-map
    width: 1700px
    height: 700px
    @media (max-width: 1400px)
        width: 1350px
    @media (max-width: 1024px)
        width:1000px
        height: 600px
    @media (max-width: 800px)
        width: 768px
    @media (max-width: 500px)
        width:450px
    @media (max-width: 376px)
        width:375px
.my-desc
    width: 1700px
    @media (max-width: 1400px)
        width: 1350px
    @media (max-width: 1024px)
        width:1000px
    @media (max-width: 800px)
        width: 768px
    @media (max-width: 500px)
        width:380px
    @media (max-width: 376px)
        width:350px
</style>
