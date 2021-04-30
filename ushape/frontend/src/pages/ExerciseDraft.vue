<template>
    <div>
    <h5 class="text-weight-bold">{{ exContent[myKey].title }}</h5>
    <div class="row q-mb-xl" v-for="index in exContent[myKey].exName.length" :key="index">
      <div class="col-12 col-md-8 "><q-img class="my-gif shadow-21" :src="'/img/' + exContent[myKey].exGif[index-1]"/></div>
      <div class="col-12 col-md-4"><h4 class="text-weight-bold"> {{ exContent[myKey].exName[index-1]}}</h4>
      <h6 class="text-weight-light float-left">{{ exContent[myKey].exDescription[index-1]}}</h6>
      </div>
      </div>
    </div>
</template>

<script>
export default {
  props: {
    myKey: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      exContent: [{
        title: 'Bench press',
        exName: [
          'Dumb-bell bench press',
          'Lying fly',
          'Incline fly',
          'Incline bench press',
          'Decline bench press'
        ],
        exDescription: [
          'Lie down on your back on a bench and hold 2 dumbbells at chest level along your body, palms facing your feet.Raise the dumbbells straight up until your elbows are close to being locked and lower them back slowly after a short pause.Breathe out when raising the dumbbells and breathe in when lowering them back.',
          'Lie down on your back on the bench and grab one dumbbell with each hand at body height, elbows just slightly arched.Raise the dumbbells until they are side by side on top of you and slowly lower them back after a short pause.Try to maintain the same angle in your elbows throughout.',
          'Lie down on your back on an incline bench and grab one dumbbell with each hand at body height, elbows just slightly arched.Raise the dumbbells until they are side by side on top of you and slowly lower them back after a short pause.Try to maintain the same angle in your elbows throughout.',
          'Lie down on your back on an inclined bench and hold 2 dumbbells at chest level along your body, palms facing forward.Raise the dumbbells straight up until your elbows are close to being locked and lower them back slowly after a short pause.Breathe out when raising the dumbbells and breathe in when lowering them back.',
          'Lie down on your back on a decline bench and hold 2 dumbbells at chest level, palms facing forward.Raise the dumbbells straight up until your elbows are close to being locked and lower them back slowly after a short pause.Breathe out when raising the dumbbells and breathe in when lowering them back.'
        ],
        exGif: [
          'bench_press_dumbbell.gif',
          'lying_fly.gif',
          'incline_fly.gif',
          'incline_bench_press.gif',
          'incline_bench_press.gif'
        ]
      }]
    }
  }
}
</script>

<style lang="sass">
.my-gif
    height:100%
    width:100%
    @media (min-width: 1024px)
        width:80%
</style>
