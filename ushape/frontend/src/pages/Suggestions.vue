<template>
<div>
     <div class="q-pa-md row q-gutter-md">
    <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs">
          <div class="text-overline">Product</div>
          <div class="text-h5 q-mt-sm q-mb-xs">Gym gloves</div>
          <div class="text-caption text-grey">
            Pick up a pair of gym gloves to protect your hands. They protect you from injuries and they cover you from bruises. Protection comes first!
          </div>
        </q-card-section>

        <q-card-section class="col-5 flex flex-center">
          <q-img
            class="rounded-borders"
            src="imgs/gloves.jpg"
          />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-btn round icon="sports_mma" />
        <q-btn color="primary">
          Buy now
        </q-btn>
      </q-card-actions>
    </q-card>

    <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs">
          <div class="text-overline">Dining place</div>
          <div class="text-h5 q-mt-sm q-mb-xs">Barca Vegan Restaurant</div>
          <div class="text-caption text-grey">
            At Barca you will find the most diverse raw vegan menu in Bucharest!
Whether you have already chosen a healthy diet or you want to experience raw vegan or vegetarian cuisine, the diversity of the menu is essential both from the perspective of nutrients and from the perspective of combinations of tastes and flavors.
Intended to give you live food, but also to stimulate the senses, the dishes on the Barca menu prove that the raw vegan / vegetarian style is far from boring. On the contrary!
          </div>
        </q-card-section>

        <q-card-section class="col-5 flex flex-center">
          <q-img
            class="rounded-borders"
            src="imgs/barca.jpg"
          />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-btn color="teal" round icon="menu_book" />
        <q-btn color="brown">
          Reserve
        </q-btn>
      </q-card-actions>
    </q-card>

        <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs">
          <div class="text-overline">Event</div>
          <div class="text-h5 q-mt-sm q-mb-xs">The Color Run</div>
          <div class="text-caption text-grey">
            The Color Run, also known as the Happiest 5K on the Planet, is a unique event that celebrates healthiness, happiness, and individuality. Now the largest running series in the world, The Color Run has been experienced by over 8 million runners worldwide in 50+ countries.
          </div>
        </q-card-section>

        <q-card-section class="col-5 flex flex-center">
          <q-img
            class="rounded-borders"
            src="imgs/colorrun.jpg"
          />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-btn color="orange" round icon="event" />
        <q-btn >
          7:30PM
        </q-btn>
        <q-btn color="pink">
          Join
        </q-btn>
      </q-card-actions>
    </q-card>

    <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs">
          <div class="text-overline">Professional trainer</div>
          <div class="text-h5 q-mt-sm q-mb-xs">Joanna Soh</div>
          <div class="text-caption text-grey">
            For all of the benefits of having a personal trainer without having to step a foot over your front doorstep, Joanna Soh is one of the best YouTube fitness vloggers to subscribe too.
            If you find that exercise challenges are the best way to get you motivated, then you’ll absolutely love Joanna’s content.
            Her health and fitness YouTube channels filled with exciting exercise challenges, such as her ‘Burn 10,000 calories in 30 days’ video or the ‘1000 cardio and core burn challenge’.
          </div>
        </q-card-section>

        <q-card-section class="col-5 flex flex-center">
          <q-img
            class="rounded-borders"
            src="imgs/joannasoh.jpg"
          />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-btn color="red" round icon="smart_display" />
        <q-btn flat>
          2.48M Subscribers
        </q-btn>
      </q-card-actions>
    </q-card>
  </div>
<div class="q-pa-md q-gutter-sm">
    <q-carousel
      animated
      v-model="slide"
      infinite
      height="500px"
    >
      <q-carousel-slide name="lifting">
        <q-video
          class="absolute-full"
          src="https://www.youtube.com/embed/sD-tzrVZvrY"
        />
      </q-carousel-slide>

      <q-carousel-slide name="running">
        <q-video
          class="absolute-full"
          src="https://www.youtube.com/embed/Yir4WyDi8rU"
        />
      </q-carousel-slide>

      <q-carousel-slide name="yoga">
        <q-video
          class="absolute-full"
          src="https://www.youtube.com/embed/2RTZNLL0wss"
        />
      </q-carousel-slide>
    </q-carousel>

    <div class="row justify-center">
      <q-btn-toggle
        glossy
        v-model="slide"
        :options="[
          { label: 'Heavy lifting', value: 'lifting' },
          { label: 'Running', value: 'running' },
          { label: 'Yoga', value: 'yoga' }
        ]"
      />
    </div>
  </div>
</div>
</template>
<script>
export default {
  data () {
    return {
      slide: 1
    }
  }
}
</script>
<style scoped lang="sass">
.my-card
  width: 100%
  max-width: 775px
</style>
