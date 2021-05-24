// import {
//   extend,
//   ValidationObserver,
//   ValidationProvider
// } from 'vee-validate'

// export default async ({ Vue }) => {
// // Register it globally
//   Vue.component('ValidationProvider', ValidationProvider)
//   Vue.component('ValidationObserver', ValidationObserver)
// }

// // Add custom rule
// extend('minMaxValue', {
//   validate: (value, {
//     min,
//     max
//   }) => {
//     return value >= Number(min) && value <= Number(max)
//   },
//   message: (fieldName, {
//     min,
//     max
//   }) => {
//     return `${fieldName} must be between ${min} and ${max}`
//   },
//   params: ['min', 'max']
// })
