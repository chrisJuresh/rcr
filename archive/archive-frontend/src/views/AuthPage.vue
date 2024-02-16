<template>
  <div class="auth-page">
    <form @submit.prevent="handleSubmit">
      <label for="username">Email</label>
      <input id="username" v-model="username" type="text" required>

      <label for="password">Password</label>
      <input id="password" v-model="password" type="password" required>

      <button type="button" @click="handleLogin">Login</button>
      <button type="button" @click="handleRegister">Register</button>
    </form>
   <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div> 
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    async handleLogin() {
      await this.login();
    },
    async handleRegister() {
      await this.register();
    },
async login() {
    try {
        const response = await axios.post('http://localhost:8000/login/', {
            username: this.username,
            password: this.password
        });
        localStorage.setItem('token', response.data.token);
        axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;
        this.$router.push('/profile'); 
    } catch (error) {
        if (error.response && error.response.status === 400) {
            this.errorMessage = 'Invalid Credentials';
        } else {
            this.errorMessage = 'An error occurred during login';
        }
        console.error(error);
    }
},
async register() {
    try {
        const response = await axios.post('http://localhost:8000/register/', {
            username: this.username,
            password: this.password
        });
        localStorage.setItem('token', response.data.token);
        axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;
        this.$router.push('/profile'); 
    } catch (error) {
        if (error.response && error.response.status === 400) {
            if (error.response.data.username) {
                this.errorMessage = 'Email is already registered';
            } else {
                this.errorMessage = 'Invalid data';
            }
        } else {
            this.errorMessage = 'An error occurred during registration';
        }
        console.error(error);
    }
}
  }
}
</script>
<style scoped>
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.auth-page form {
  display: flex;
  flex-direction: column;
  width: 300px;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  background-color: white;
}

.auth-page form label {
  margin-bottom: 10px;
}

.auth-page form input {
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.auth-page form button {
  padding: 10px;
  border-radius: 5px;
  border: none;
  color: white;
  background-color: #007bff;
  cursor: pointer;
  margin-bottom: 5px;
}

.auth-page form button:disabled {
  background-color: #ccc;
}

.error-message {
  color: red;
  margin-left: 20px;
}
</style>