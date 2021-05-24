var vbs = {

  username: 'notLoggedIn'
}
export default async ({ Vue }) => {
  Vue.prototype.$vbs = vbs
}
export { vbs }
