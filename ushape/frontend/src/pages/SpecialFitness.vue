<template>
<div class="q-pa-md row q-gutter-md">
    <q-card dark class="my-card">
      <q-card-section>
        <h2>Special fitness</h2>
      </q-card-section>
    </q-card>

    <q-card
      class="my-card text-white bg-primary"
    >
      <q-card-section>
        <div class="text-h3">What is it?</div>
        <div class="text-overline">quick summary</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        This page is dedicated to people with different disabilities.You don’t need to have full mobility to experience the health benefits of exercise.
        If injury, disability, illness, or weight problems have limited your mobility, there are still plenty of ways you can use exercise to boost your mood, ease depression, relieve stress and anxiety,
        enhance your self-esteem.
      </q-card-section>
    </q-card>

    <q-card dark bordered class="bg-red-9 my-card">
      <q-card-section>
        <div class="text-h6">Cardiovascular exercises</div>
      </q-card-section>

      <q-separator dark inset />

      <q-card-section>
        These exercises raise your heart rate and increase your endurance.
        These can include walking, running, cycling, dancing, tennis, swimming, water aerobics, or “aquajogging”.
        Many people with mobility issues find exercising in water especially beneficial as it supports the body and reduces the risk of muscle or joint discomfort.
        Even if you’re confined to a chair or wheelchair, it’s still possible to perform cardiovascular exercise.
      </q-card-section>
    </q-card>

    <q-card flat bordered class="my-card">
      <q-card-section>
        <div class="text-h6">Strength training exercises</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        Strength training exercises involve using weights or other resistance to build muscle and bone mass, improve balance, and prevent falls.
        If you have limited mobility in your legs, your focus will be on upper body strength training.
      </q-card-section>

      <q-separator inset />

      <q-card-section>
        Similarly, if you have a shoulder injury, for example, your focus will be more on strength training your legs and core.
      </q-card-section>
    </q-card>

    <q-card dark bordered class="bg-grey-9 my-card">
      <q-card-section>
        <div class="text-h6">Flexibility exercises</div>
      </q-card-section>

      <q-separator dark inset />

      <q-card-section>
        Flexibility exercises help enhance your range of motion, prevent injury, and reduce pain and stiffness. These may include stretching exercises and yoga.</q-card-section>
        <q-card-section>
        Even if you have limited mobility in your legs, for example, you may still benefit from stretches and flexibility exercises to prevent or delay further muscle atrophy.
      </q-card-section>
    </q-card>

    <q-card flat bordered class="my-card bg-green-7">
      <q-card-section>
        <div class="text-h6">Starting an exercise routine</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
       Start slow and gradually increase your activity level. Start with an activity you enjoy, go at your own pace, and keep your goals manageable.
        Accomplishing even the smallest fitness goals will help you gain body confidence and keep you motivated.
      </q-card-section>

      <q-separator inset />

      <q-card-section>
        Make exercise part of your daily life. Plan to exercise at the same time every day and combine a variety of exercises to keep you from getting bored.
      </q-card-section>
    </q-card>

    <q-card class="my-card bg-orange-9" dark bordered>
      <q-card-section horizontal>
        <q-card-section>
          <div class="text-h6">Overcoming mental barriers to exercise</div>
          <br>
          As well as the physical challenges you face, you may also experience mental or emotional barriers to exercising.
          It’s common for people to feel self-conscious about their weight, disability, illness, or injury, and want to avoid working out in public places.
           Some older people find that they’re fearful about falling or otherwise injuring themselves.
        </q-card-section>

        <q-img
          class="col-5"
          src="imgs/mental.jpg"
        />
      </q-card-section>
    </q-card>
     <q-card flat dark bordered class="my-card bg-secondary">
         <q-card-section>
        <div class="text-h6">Don't stop, keep going!</div>
      </q-card-section>
      <q-list bordered separator>
      <q-item clickable v-ripple>
        <q-item-section>Be proud when you make the effort to exercise</q-item-section>
      </q-item>

      <q-item clickable v-ripple>
        <q-item-section>
          <q-item-label>Don’t focus on your mobility or health issue</q-item-label>
          <q-item-label caption>You got this!</q-item-label>
        </q-item-section>
      </q-item>

      <q-item clickable v-ripple>
        <q-item-section>
          <q-item-label overline>REMEMBER</q-item-label>
          <q-item-label>The more physical challenges you face, the more creative you’ll need to be</q-item-label>
        </q-item-section>
      </q-item>

        <q-item clickable v-ripple>
        <q-item-section>Start by choosing exercises that require little to no skill: walking, cycling on stationary bike</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>It's okay to take a break. Take your time, but never quit</q-item-section>
      </q-item>
    </q-list>
    </q-card>
  </div>
</template>
<script>
export default {
  data () {
    return {
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    }
  }
}
</script>
<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 775px
</style>
