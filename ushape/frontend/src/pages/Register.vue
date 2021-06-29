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
        :rules="[ val => val && val.length > 0 || 'Please type your username',
                  val => val.length > 4 || 'Username must contain more than 4 characters']"
      />
      <q-input
        ref="email"
        name = "email"
        filled
        v-model="user.email"
        label="Your e-mail *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please enter your e-mail']"
        class="q-mt-xs"
      />
      <q-input
        ref="password"
        name = "password"
        filled
        :type="isPwd ? 'password' : 'text'"
        v-model="user.password"
        label="Your password *"
        lazy-rules
        :rules="[val => val.length > 7 || 'Password too short']"
        class="q-mt-xs"
      >
      <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template></q-input>
      <q-input
        ref="password2"
        name = "password2"
        filled
        :type="isPwd2 ? 'password' : 'text'"
        v-model="user.password2"
        label="Repeat your password *"
        lazy-rules
        :rules="[val => val.length > 7 || 'Passwords must be identical']"
        class="q-mt-xs">
        <template v-slot:append>
          <q-icon
            :name="isPwd2 ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd2 = !isPwd2"
          />
        </template></q-input>
      <q-input
        ref="first_name"
        name = "first_name"
        filled
        v-model="user.first_name"
        label="Your first name *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your first name']"
        class="q-mt-xs"
      />
      <q-input
        ref="last_name"
        name = "last_name"
        filled
        v-model="user.last_name"
        label="Your last name *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your last name']"
        class="q-mt-xs"
      />
       <q-toggle v-model="accept" label="I accept the license and terms" />
      <div>
        <q-btn label="Submit" type="submit" color="primary" />
        <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </form>
  </div>
</template>

<script>
import User from '../models/user'

export default {
  name: 'Register',
  data   () {
    return {
      user: new User('', '', '', '', '', ''),
      submitted: false,
      successful: false,
      message: '',
      isPwd: true,
      isPwd2: true,
      accept: false
    }
  },
  computed: {
    loggedIn () {
      return this.$store.state.auth.status.loggedIn
    }
  },
  mounted () {
    if (this.loggedIn) {
      this.$router.push('/journal')
    }
  },
  methods: {
    onSubmit () {
      this.$refs.username.validate()
      this.$refs.email.validate()
      this.$refs.password.validate()
      this.$refs.password2.validate()
      this.$refs.first_name.validate()
      this.$refs.last_name.validate()

      if (this.$refs.username.hasError || this.$refs.email.hasError || this.$refs.password.hasError || this.$refs.password2.hasError || this.$refs.first_name.hasError || this.$refs.last_name.hasError) {
        this.formHasError = true
      } else if (this.accept !== true) {
        this.$q.notify({
          color: 'negative',
          message: 'Please accept license and terms'
        })
      } else {
        this.message = ''
        this.submitted = true
        this.$store.state.auth.usernameName = this.user.username
        this.$store.dispatch('auth/register', this.user).then(
          data => {
            this.$q.notify({
              icon: 'done',
              color: 'positive',
              message: 'Submitted'
            })
            this.message = data.message
            this.successful = true
            this.$store.state.auth.status.loggedIn = true
            this.$router.push('/journal')
          },
          error => {
            this.$q.notify({
              color: 'negative',
              message: 'Something went wrong!'
            })
            this.message =
              (error.response && error.response.data) ||
              error.message ||
              error.toString()
            this.successful = false
          }
        )
      }
    },

    onReset () {
      this.user.username = null
      this.user.email = null
      this.user.password = null
      this.user.password2 = null
      this.user.first_name = null
      this.user.last_name = null

      this.$refs.username.resetValidation()
      this.$refs.email.resetValidation()
      this.$refs.password.resetValidation()
      this.$refs.password2.resetValidation()
      this.$refs.first_name.resetValidation()
      this.$refs.last_name.resetValidation()
    }
  }
}
// NOTE TO SELF: you have to set validations to username, password, email
</script>
<style scoped>
form { margin: 0 auto;
max-width:50%;}
</style>
