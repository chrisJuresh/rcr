<template>
    <h1 v-if="user">Edit: {{ user.username }}</h1>
  <div>
    <div v-if="user">
      <form @submit.prevent="updateProfile">
        <label for="firstName">First Name:</label>
        <input id="firstName" v-model="user.first_name" type="text" required />

        <label for="lastName">Last Name:</label>
        <input id="lastName" v-model="user.last_name" type="text" required />

        <label for="trusts">Trust:</label>
        <select id="trusts" v-model="user.trust" required>
          <option disabled value="">Please select a trust</option>
          <option v-for="trust in trusts" :key="trust.id" :value="trust.id">
            {{ trust.name }}
          </option>
        </select>


<label for="roles">Title (hold ctrl to select multiple| message the rcr for permission to other roles):</label>
<select id="roles" v-model="user.roles" multiple>
  <option 
    v-for="role in roles" 
    :value="role.id" 
    :key="role.id" 
    :class="{ 'highlight-role': user.roles.includes(role.id) }" 
    :disabled="!allowedRoles.includes(role.name)"
  >
    {{ role.name }}
  </option>
</select>
<button type="submit">Update</button>
      </form>
      <button>
  <router-link to="/panel">Go to Panel</router-link>
</button>
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
      roles: [],
    };
  },
  computed: {
    allowedRoles() {
      const roles = [];
    roles.push('TRUST_EMPLOYEE');
    console.log(this.user); 
      if (this.user.can_be_reviewer) roles.push('REVIEWER');
      if (this.user.can_be_representative) roles.push('REPRESENTATIVE');
      if (this.user.can_be_rcr_employee) roles.push('RCR_EMPLOYEE');
      return roles;
    }
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

    const rolesResponse = await axios.get('http://localhost:8000/roles/', {
      headers: {
        'Authorization': `Token ${token}`
      }
    });
    this.roles = rolesResponse.data;
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

.highlight-role {
  background-color: #73d177;
}
</style>