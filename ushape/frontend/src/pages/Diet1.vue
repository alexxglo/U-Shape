<template>
   <div class="q-px-lg q-pb-md">
    <q-timeline color="primary">
      <q-timeline-entry heading>
        {{content[componentNo].title}}
      </q-timeline-entry>
      <text-body1 v-html="content[componentNo].description"></text-body1>
      <q-timeline-entry>
        <template v-slot:title>
          Breakfast
        </template>
        <template v-slot:subtitle>
         7:00-10:00 AM
        </template>
        <div>
            <p> Suggestions: </p>
            <q-list bordered separator>
      <q-item v-ripple v-for="text in content[componentNo].breakfast"
      :key="text">
      <q-item-selection>{{text}}</q-item-selection>
      </q-item>
      </q-list>
        </div>
      </q-timeline-entry>

      <q-timeline-entry>
        <template v-slot:title>
          Lunch
        </template>
        <template v-slot:subtitle>
          12:00 - 2:00 PM
        </template>
        <div>
            <p> Suggestions: </p>
            <q-list bordered separator>
      <q-item v-ripple v-for="text in content[componentNo].lunch" :key="text">
        <q-item-section>{{text}}</q-item-section>
      </q-item>
      </q-list>
        </div>
      </q-timeline-entry>

      <q-timeline-entry>
        <template v-slot:title>
          Dinner
        </template>
        <template v-slot:subtitle>
          5:00 - 7:00 PM
        </template>
        <p>Suggestions:</p>
       <div>
            <q-list bordered separator>
      <q-item v-ripple v-for="text in content[componentNo].lunch" :key="text">
        <q-item-section>{{text}}</q-item-section>
      </q-item>
      </q-list>
        </div>
      </q-timeline-entry>

      <q-timeline-entry>
        <template v-slot:title>
          Healthy snacks
        </template>
        <template v-slot:subtitle>
          In-between
        </template>
        <p>Suggestions:</p>
         <div>
            <q-list bordered separator>
      <q-item v-ripple v-for="text in content[componentNo].snacks" :key="text">
        <q-item-section>{{text}}</q-item-section>
      </q-item>
      </q-list>
        </div>
      </q-timeline-entry>
    </q-timeline>
  </div>
</template>

<script>

export default {
  props: {
    componentNo: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      content: [{
        title: 'Keto diet',
        description: 'The ketogenic diet (or keto diet, for short) is a low carb, high fat diet that offers many health benefits.In fact, many studies show that this type of diet can help you lose weight and improve your health.<br>Ketogenic diets may even have benefits against diabetes, cancer, epilepsy, and Alzheimer’s disease.',
        breakfast: [
          'Veggie and egg muffins with tomatoes',
          'Egg, tomato, basil and spinach omelet',
          'Nut milk chiat pudding topped with coconut and blackberries',
          'Omelet with avocado, salsa, peppers, onion and spices',
          'Sugar-free greek, whole milk yogurt with peanut butter, cocoa powder, and berries',
          'Cream cheese pancakes with blueberries and a side of grilled mushrooms',
          'Fried eggs with mushrooms'
        ],
        lunch: [
          'Chicken salad with olive oil, feta cheese, olives and a side salad',
          'Almond milk, peanut butter, spinach, cocoa powder, and stevia milkshake with a side of sliced strawberries',
          'Avocado shrimp salad',
          'Nuts and celery sticks with guacamole and salsa',
          'Ground beef lettuce wrap tacos with sliced bell peppers',
          'Zucchini and beet “noodle” salad',
          'Sesame chicken and broccoli'
        ],
        dinner: [
          'Salmon with asparagus cooked in butter',
          'Cheese-shell tacos with salsa',
          'Pork chops with Parmesan cheese, broccoli, and salad',
          'Chicken stuffed with pesto and cream cheese, and a side of grilled zucchini',
          'Loaded cauliflower and mixed veggies',
          'White fish cooked in coconut oil with kale and toasted pine nuts',
          'Spaghetti squash Bolognese'
        ],
        snacks: [
          '90% dark chocolate',
          'Full-fat Greek yogurt mixed with nut butter and cocoa powder',
          'Strawberries and plain cottage cheese',
          'Nuts or seeds',
          'Olives',
          'Cheese',
          'Smaller portions of leftover meals'
        ]
      }
      ]
    }
  }
}
</script>
