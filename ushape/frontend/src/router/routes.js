const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/test', component: () => import('pages/Test.vue') },
      { path: '/diets', component: () => import('pages/Diets.vue') },
      { path: '/exercises', component: () => import('pages/Exercises.vue') },
      { path: '/calorie-calculator', component: () => import('pages/CalorieCalculator.vue') },
      { path: '/journal', component: () => import('pages/Journal.vue') },
      { path: '/login', component: () => import('pages/Login.vue') },
      { path: '/register', component: () => import('pages/Register.vue') }
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
