import axios from 'axios'
// AUTHENTICATION SERVICE
const API_URL = 'http://localhost:8000/api/'

class AuthService {
  login (user) {
    return axios
      .post(API_URL + 'login/', {
        username: user.username,
        password: user.password
      })
      .then(response => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data))
          console.log(response.data)
        }

        return response.data
      })
  }

  logout () {
    localStorage.removeItem('user')
  }

  register (user) {
    return axios.post(API_URL + 'register/', {
      username: user.username,
      password: user.password,
      password2: user.password2,
      email: user.email,
      first_name: user.first_name,
      last_name: user.last_name
    })
  }
}

export default new AuthService()
