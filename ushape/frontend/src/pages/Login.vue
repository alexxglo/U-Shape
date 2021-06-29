<template>
 <div class = "justify-center align-center q-mt-xl">
    <div class="flex flex-center q-mb-md">
    <q-img class="q-mt-md" src="~assets/ushapelogo.png" style="width:240px; height:160px;"/>
    </div>
    <form @submit.prevent.stop="onSubmit" @reset.prevent.stop="onReset" class="justify-center items-center">
      <q-input
        ref="username"
        name = "username"
        filled
        v-model="user.username"
        label="Your username *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your username']"
      />
      <q-input
        ref="password"
        name = "password"
        filled
        :type="isPwd ? 'password' : 'text'"
        v-model="user.password"
        label="Your password *"
        lazy-rules
        :rules="[val => val.length > 0 || 'Please type your password']"
        class="q-mt-xs"
      >
      <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template></q-input>
       <div class="float-left q-mt-xs">
        <q-btn label="Submit" type="submit" color="primary" />
      </div>
    </form>
 </div>
</template>

<script>
import User from '../models/user'
export default {
  name: 'Login',
  data () {
    return {
      user: new User('', ''),
      loading: false,
      message: '',
      isPwd: true,
      accept: true
    }
  },
  computed: {
    loggedIn () {
      return this.$store.state.auth.status.loggedIn
    }
  },
  created () {
    if (this.loggedIn) {
      this.$router.push('/journal')
    }
  },
  methods: {
    onSubmit () {
      this.$refs.username.validate()
      this.$refs.password.validate()
      console.log(this.user.username)
      if (this.$refs.username.hasError || this.$refs.password.hasError) {
        this.formHasError = true
      } else if (this.accept !== true) {
        this.$q.notify({
          color: 'negative',
          message: 'Oops! Something went wrong. Please try again'
        })
      } else {
        this.loading = true
        if (this.user.username && this.user.password) {
          this.$store.dispatch('auth/login', this.user).then(
            () => {
              this.$store.state.auth.usernameName = this.user.username
              this.$router.push('/journal')
              console.log(this.user.username)
              this.$q.notify({
                icon: 'done',
                color: 'positive',
                message: 'Logged in'
              })
            },
            error => {
              this.loading = false
              this.$q.notify({
                color: 'negative',
                message: 'Username or password is incorrect'
              })
              this.message =
                (error.response && error.response.data && error.response.data.message) ||
                error.message ||
                error.toString()
            }
          )
        }
      }
    }
  }
}
</script>
<style scoped>
form { margin: 0 auto;
max-width:50%;}
</style>
