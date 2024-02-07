<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Job Title</th>
          <th>Description</th>
          <!-- Add more columns as needed -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in jobs" :key="job.id">
          <td>{{ job.title }}</td>
          <td>{{ job.description }}</td>
          <!-- Add more data cells as needed -->
        </tr>
      </tbody>
    </table>
  </div>
  <router-link to="/newJD">
  <button>Create New JD</button>
</router-link>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      jobs: [],
    };
  },
  async created() {
    const response = await axios.get('http://localhost:8000/jds/');
    this.jobs = response.data;
  },
};
</script>

<style scoped>
.table-container {
  max-height: 400px; 
  overflow-y: auto;
}
</style>