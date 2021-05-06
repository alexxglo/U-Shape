<template>
   <div class="q-px-lg q-pb-md">
    <q-timeline color="primary">
      <q-timeline-entry heading>
        {{content[componentNo].title}}
        <br>
        <div class="text-subtitle1 text-italic">{{content[componentNo].dietType}}</div>
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
        dietType: 'Low-carbohydrate / High-fat diet',
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
      },
      {
        title: 'Paleo diet',
        dietType: 'Food-specific diet',
        description: 'The paleo diet is an eating plan that mimics how prehistoric humans may have eaten. It involves eating whole foods that people could theoretically hunt or gather.<br>The paleo diet is not safe for everyone. Doctors do not know its effects on children, pregnant women, or older adults. People with chronic conditions, such as inflammatory bowel disease, should also speak to a doctor before trying a paleo diet.',
        breakfast: [
          'Avocado, kale, banana, and apple smoothie with almond milk',
          'Scrambled eggs with wilted spinach, grilled tomatoes, and pumpkin seeds.',
          'Chopped bananas with blueberries and almonds.',
          'Broccoli fried in coconut oil with toasted almonds and a poached egg',
          'Coconut milk, mixed berries, and spinach smoothie',
          'Bacon, eggs, and tomatoes fried in olive oil',
          'Spring onion, tomato, and mushroom omelet'
        ],
        lunch: [
          'Mixed salad leaves with fried seabass, pumpkin seeds, and an olive oil dressing',
          'Mixed salad leaves with leftover roast chicken and an olive oil dressing',
          'Mixed salad leaves with leftover salmon and an olive oil dressing',
          'Mixed salad with tuna, boiled eggs, seeds, and olive oil',
          'Butternut squash, broccoli, and tomato omelet with mixed salad',
          'Mixed vegetable and chicken soup with turmeric',
          'Mixed salad with chicken, avocado, seeds, and olive oil'
        ],
        dinner: [
          'Roast chicken with a stuffing of onions, carrots, and rosemary',
          'Oven-baked salmon with asparagus and broccoli fried in coconut oil',
          'Beef stir-fry with mixed peppers, using coconut oil to fry',
          'Harissa-baked chicken wings with steamed broccoli',
          'Red pepper, broccoli, baby corn, and salmon stir-fry',
          'Grilled lamb chops with wilted spinach and spiced red cabbage',
          'Slow-cooked beef stew with mixed vegetables'
        ],
        snacks: [
          'Whole fruits such as apples, pears, bananas, and oranges',
          'Fresh veggie sticks',
          'Hard-boiled eggs and veggies',
          'Smoked almonds',
          'Vegetable chips',
          'Pumpkin and sunflower seeds',
          'Seaweed snacks'
        ]
      },
      {
        title: 'F-Plan diet',
        dietType: 'Low-fat / High fiber diet',
        description: 'The F-plan is a high fibre diet designed to induce healthy weight loss, created in the 1980s by British author Audrey Eyton. <br> The diet works by restricting the daily intake of calories to less than 1,500 whilst consuming well-above the recommended level of dietary fibre. The fibre has a number of beneficial effects, such as making the dieter feel "full" for much longer than normal, reducing the urge to overeat, and promoting a healthy digestive system.',
        breakfast: [
          'Cereal/fruit mix with low fat milk, piece of fresh fruit',
          'Green smoothie, ',
          'Apple cinnamon chia pudding',
          'Baked banana and nut oatmeal cup',
          'Muesli with grated apple',
          'Bran with mango',
          'Orange, grapefruit, scrambled egg on toast'
        ],
        lunch: [
          'Nutty coleslaw, fresh fruit',
          'White bean & avocado toast',
          'Brussels sprouts salad with crunchy chickpeas',
          'Chicken & tomato sandwich, orange',
          ' Avocado & prawn salad',
          'Lentil soup and a roll',
          'Waldorf salad'
        ],
        dinner: [
          'Skinless baked chicken, baked potato, mixed salad',
          'Roasted chicken, winter squash, mixed Greens',
          'Salmon, spinach with a baked potato',
          'Pasta Primavera',
          'Paprika chicken',
          'Chicken, potatoes, broccoli, peach slices with yoghurt',
          'Tarragon chicken & rice'
        ],
        snacks: [
          'Fruits',
          'Crudites & cream cheese',
          'Mixed salad',
          'Crisps',
          'Yoghurt, a handful of sultanas',
          'Crispbread, tomatoes, pineapple chunks',
          'Strawberries, banana & yoghurt'
        ]
      }
      ]
    }
  }
}
</script>
