<template>
  <div>
      <div class="dimmed">
      <Journal/></div>
  <div class="q-pa-md q-gutter-md relative-center">
    <q-card class="bg-grey-3 relative-position fixed-center card-example">
      <q-card-section class="q-pb-none">
        <div v-if="visible === true" class="text-h3">Your photo is uploading...</div>
        <div v-else class="text-h3 q-mt-md"> Uploaded!</div>
      </q-card-section>

      <q-card-section>
        <transition
          appear
          enter-active-class="animated fadeIn"
          leave-active-class="animated fadeOut"
        >
          <div v-show="showSimulatedReturnData">
            <h5 class="q-mb-xl">Your photo has been uploaded! Press 'Continue' button to see your journal </h5>
            <q-btn color="primary" @click="redirect()" class="absolute-bottom q-ml-md q-mt-xl">Continue
            </q-btn>
          </div>
        </transition>
      </q-card-section>

      <q-inner-loading :showing="visible">
        <q-spinner-gears size="50px" color="primary" />
      </q-inner-loading>
    </q-card>
  </div>
  </div>
</template>

<script>
import Journal from './Journal'
export default {
  components: { Journal },
  data () {
    var visible = false
    var showSimulatedReturnData = false
    return {
      visible,
      showSimulatedReturnData
    }
  },
  methods: {
    showTextLoading () {
      this.visible = true
      this.showSimulatedReturnData = false
      setTimeout(() => {
        this.visible = false
        this.showSimulatedReturnData = true
      }, 4000)
    },
    redirect () {
      this.$router.push('/journal')
    }
  },
  mounted () {
    this.showTextLoading()
  }
}
</script>

<style lang="scss" scoped>
.card-example
{
  @media screen and (min-width: 688px) {
      width: 600px;
      height: 340px;
  }

  @media screen and (max-width: 687px) {
  width: 450px;
  height: 320px;
  }

  @media screen and (max-width: 420px) {
  width: 450px;
  height: 320px;
  }
  @media screen and (max-width: 380px) {
  width: 400px;
  height: 320px;
  }
  @media screen and (max-width: 320px) {
  width: 350px;
  height: 340px;
  }
  @media screen and (max-width: 280px) {
  width: 310px;
  height: 340px;
  }
}
</style>
