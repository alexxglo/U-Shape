<template>
   <div class="q-px-lg q-pb-md">
    <q-timeline color="primary">
      <q-timeline-entry heading>
        Keto diet
      </q-timeline-entry>
      <text-body1>The ketogenic diet (or keto diet, for short) is a low carb, high fat diet that offers many health benefits.
In fact, many studies show that this type of diet can help you lose weight and improve your health.<br>
Ketogenic diets may even have benefits against diabetes, cancer, epilepsy, and Alzheimer’s disease.</text-body1>

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
      <q-item clickable v-ripple>
        <q-item-section>Veggie and egg muffins with tomatoes</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Egg, tomato, basil and spinach omelet</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Nut milk chiat pudding topped with coconut and blackberries</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Omelet with avocado, salsa, peppers, onion and spices</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Sugar-free greek, whole milk yogurt with peanut butter, cocoa powder, and berries</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Cream cheese pancakes with blueberries and a side of grilled mushrooms</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Fried eggs with mushrooms</q-item-section>
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
      <q-item clickable v-ripple>
        <q-item-section>Chicken salad with olive oil, feta cheese, olives and a side salad</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Almond milk, peanut butter, spinach, cocoa powder, and stevia milkshake with a side of sliced strawberries</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Avocado shrimp salad</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Nuts and celery sticks with guacamole and salsa</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section> Ground beef lettuce wrap tacos with sliced bell peppers</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Zucchini and beet “noodle” salad</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Sesame chicken and broccoli</q-item-section>
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
      <q-item clickable v-ripple>
        <q-item-section>Salmon with asparagus cooked in butter</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Cheese-shell tacos with salsa</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Pork chops with Parmesan cheese, broccoli, and salad</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Chicken stuffed with pesto and cream cheese, and a side of grilled zucchini</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Loaded cauliflower and mixed veggies</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>White fish cooked in coconut oil with kale and toasted pine nuts</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Spaghetti squash Bolognese</q-item-section>
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
        <p>Suggestions</p>
         <div>
            <q-list bordered separator>
      <q-item clickable v-ripple>
        <q-item-section>90% dark chocolate</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Full-fat Greek yogurt mixed with nut butter and cocoa powder</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Strawberries and plain cottage cheese</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Nuts or seeds</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Olives</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Cheese</q-item-section>
      </q-item>
      <q-item clickable v-ripple>
        <q-item-section>Smaller portions of leftover meals</q-item-section>
      </q-item>
      </q-list>
        </div>
      </q-timeline-entry>
    </q-timeline>
  </div>
</template>

<script>

export default {

}
</script>
