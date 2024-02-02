<template>
  <div>
    <p v-if="user">{{ user.username }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: null,
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
}
};
</script>