<template>
    <div>
    <h5 class="text-weight-bold">{{ exContent[myKey].title }}</h5>
    <div class="row q-mb-xl" v-for="index in exContent[myKey].exName.length" :key="index">
      <div class="col-12 col-md-8 "><q-img class="my-gif shadow-21" :src="exContent[myKey].exGif[index-1]"/></div>
      <div class="col-12 col-md-4"><h4 class="text-weight-bold"> {{ exContent[myKey].exName[index-1]}}</h4>
      <h6 class="text-weight-light float-left" v-html="exContent[myKey].exDescription[index-1]"/>
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
        title: 'Chest exercises',
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
          'Gifs/bench_press_dumbbell.gif',
          'Gifs/lying_fly.gif',
          'Gifs/incline_fly.gif',
          'Gifs/incline_bench_press.gif',
          'Gifs/decline_bench_press.gif'
        ]
      },
      {
        title: 'Biceps and triceps exercises',
        exName: [
          'Barbell curl',
          'Preacher curl',
          'Seated alternated curl',
          'Standing landmine',
          'Triceps extension'
        ],
        exDescription: [
          'Stand tall with your chest up and core braced, holding the barbell with your hands just outside of your hips, using an underhand grip. Keeping your chest up and your elbows tight to your sides, initiate the move by raising your hands slightly so you feel your biceps become engaged. While maintaining tension on your biceps, curl the bar up to shoulder height, then give your biceps a one-second squeeze. Start to lower the bar slowly, keeping your biceps tensed and engaged to work as many muscle fibres as possible.<br> Once the bar is back in the start position, straighten your arms fully to tense your triceps to ensure that your biceps are worked through the fullest possible range of motion.',
          '<li>Set up on the preacher bench, holding a dumbbell in each hand by your shoulders with your palms facing away from you.<li> Lower the weights slowly until your arms are fully extended, then rotate your hands so your palms face towards you and curl the dumbbells back up to your shoulders.',
          '<li>Sit down on a bench and hold one dumbbell with each hand down the side of your body, palms facing each other. <li>Raise one dumbbell until it reaches your shoulder’s height and while slowly lowering it back down after a short pause, start raising the other one.<li>Try NOT to jerk your upper body in an effort to help you lift the weights.',
          '<li>Press the weight up by extending at your elbow.<li>As you extend your arm, press the weight straight forwards so that it stays in line with your shoulder.<li>At the top of the move, your elbow should as straight as possible without hyperextending. Keeping this slight bend in your elbow will keep your muscles under tension and reduce your risk of injury.<li>Pause for a moment before slowly bending at the elbow to lower the barbell back towards your shoulder.',
          '<li>Stand up and hold one dumbbell with both hands behind your head, upper arms pointing straight up.<li>Raise the dumbbell up by curling your elbows and slowly lower it back after a short pause.<li>Your upper arms should remain still throughout.'
        ],
        exGif: [
          'Gifs/barbell_curl.gif',
          'Gifs/preacher_curl.gif',
          'Gifs/seated_alternated_curl.gif',
          'Gifs/standing_landmine.gif',
          'Gifs/triceps_extension.gif'
        ]
      },
      {
        title: 'Back exercises',
        exName: [
          'Lat pulldown',
          'Seated cable row',
          'Front squat',
          'Deadlift'
        ],
        exDescription: [
          'Grasp the bar with a wide grip, looking forward with your torso upright. Retract your shoulder blades and pull the bar down in front of you to your upper chest. Squeeze your lats at the bottom of the move. Resist the temptation to lean back to aid the movement.',
          '<li>Pull the handle and weight back toward the lower abdomen while trying not to use the momentum of the row too much by moving the torso backward with the arms.<li>Target the middle to upper back by keeping your back straight and squeezing your shoulder blades together as you row, chest out.<li>Return the handle forward under tension to full stretch, remembering to keep that back straight even though flexed at the hips.',
          'Take one step backwards. Position your feet shoulder-width apart, with your toes pointing very slightly diagonally away from each other. Brace yourself, take a deep breath in to fill your chest and keep your torso strong, then bend your legs to lower into a squat. Keep your knees wide apart and heels down.',
          'Standing with your feet shoulder-width apart, grasp the bar with your hands just outside your legs. Lift the bar by driving your hips forwards, keeping a flat back. Lower the bar under control – though once you get up to really heavy weights, it’s OK to drop it on your final rep.'
        ],
        exGif: [
          'Gifs/lat_pulldown.gif',
          'Gifs/seated_cable_row.gif',
          'Gifs/front_squat.gif',
          'Gifs/deadlift.gif'
        ]
      },
      {
        title: 'Shoulder exercises',
        exName: [
          'Palms-in shoulder press',
          'Lateral raise',
          'Shoulder press',
          'Overhead press'
        ],
        exDescription: [
          '<li>Stand up and hold two dumbbells at shoulder level, palms facing each other.<li>Push the dumbbells straight up until your elbows come close to locking and lower them back down after a short pause.<li>Be careful NOT to jerk your back in an effort to help you raise the dumbbells.',
          '<li>Stand up and hold one dumbbell with each hand in front of your hips, palms facing each other.<li>Raise the dumbbells to your sides until your arms are close to being parallel to the ground and lower them back down after a short pause.<li>Try to maintain the angles in your elbows still throughout.',
          '<li>Stand up and hold two dumbbells close to your shoulders, palms facing forward.<li>Raise the dumbbells straight up until your elbows come close to locking and lower them back after a short pause.<li>Be careful NOT to jerk your back in an effort to help you raise the dumbbells.',
          'Stand tall with a barbell across the front of your shoulders. Brace your core, then press the bar directly overhead. Lower it slowly back to the start.'
        ],
        exGif: [
          'Gifs/palms_in_shoulder_press.gif',
          'Gifs/lateral_raise.gif',
          'Gifs/shoulder_press.gif',
          'Gifs/overhead_press.gif'
        ]
      },
      {
        title: 'Leg exercises',
        exName: [
          'Barbell squat',
          'Romanian deadlift',
          'Walking lunge',
          'Leg stepup'
        ],
        exDescription: [
          'Make a hip-width stance with your toes facing slightly outward. Support the barbell on the top of your trap muscles, chest up, and head facing forward.<br>Bend your knees slowly, while driving them outward and keeping your back straightened. Hinge your hips and your knees will move forward. Make sure the bar moves in a straight line up and down.',
          'Assume a shoulder-width stance while holding a bar with your palms facing down at a hip level. Arch your back, keep your shoulders back, and your knees bent slightly.<br>Move your buttocks back as far as you can as you lower the bar. Maintain the bar’s distance to your body while keeping your shoulders back, chest out and your head looking forward. Lower the bar down to about knee level, then drive the hips forward, and return to your initial position.',
          'Begin with a hip-width stance holding a dumbbell in each hand.<br>Put one leg forward, bending your knees to lower your hips. Dip until your back knee nearly meets the floor. Keep an upright posture, and avoid moving your front knee past your toes to avoid injury.<br>Put your weight on your front foot’s heel and ascend from the lunge. Switch sides and repeat.',
          'Lean forward and step up as fast as possible, jumping off the box with your right leg. Land on the right leg as you step back with your left leg. Repeat 10 times on your right leg before switching to your left. Do not use weight for this exercise.'
        ],
        exGif: [
          'Gifs/barbell_squat.gif',
          'Gifs/romanian_deadlift.gif',
          'Gifs/dumbbell_walking_lunge.gif',
          'Gifs/leg_stepup.gif'
        ]
      }
      ]
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
