<template>
  <div>
    <p v-if="user">{{ user.username }}</p>
    <div v-if="user">
      <h2>Edit Profile</h2>
      <form @submit.prevent="updateProfile">
        <label for="firstName">First Name:</label>
        <input id="firstName" v-model="user.first_name" type="text" />

        <label for="lastName">Last Name:</label>
        <input id="lastName" v-model="user.last_name" type="text" />

        <label for="trusts">Trust:</label>
        <select id="trusts" v-model="user.trust">
          <option v-for="trust in trusts" :key="trust.id" :value="trust.id">
            {{ trust.name }}
          </option>
        </select>

        <button type="submit">Update</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: null,
      trusts: [],
    };
  },
  async created() {
    const token = localStorage.getItem('token');
    const response = await axios.get('http://localhost:8000/profile/', {
      headers: {
        'Authorization': `Token ${token}`
      }
    });
    this.user = response.data;

    const trustsResponse = await axios.get('http://localhost:8000/trusts/', {
      headers: {
        'Authorization': `Token ${token}`
      }
    });
    this.trusts = trustsResponse.data;
  },
  methods: {
    async updateProfile() {
      const token = localStorage.getItem('token');
      await axios.put('http://localhost:8000/profile/', this.user, {
        headers: {
          'Authorization': `Token ${token}`
        }
      });
    }
  }
};
</script>

<style scoped>
div {
  margin: 0 auto;
  max-width: 400px;
}

h2 {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
  margin-top: 20px;
}

input {
  border: 1px solid #ccc;
  border-radius: 4px;
  height: 30px;
  margin-top: 5px;
  padding: 0 10px;
}

button {
  background-color: #4CAF50;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
  font-size: 16px;
  height: 40px;
  margin-top: 30px;
}

button:hover {
  background-color: #45a049;
}
</style>