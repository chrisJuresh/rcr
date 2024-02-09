<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th class="job-title">Job Title</th>
          <th class="submission-date">Submission Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in jobs" :key="job.id">
          <td class="job-title">{{ job.document }}</td>
          <td class="submission-date">{{ formatDate(job.submission_date) }}</td>
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
  methods: {
    formatDate(isoDateString) {
      const date = new Date(isoDateString);
      return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
    }
  },
  async created() {
    const token = localStorage.getItem('token');
  
    const response = await axios.get('http://localhost:8000/jds/', {
      headers: {
        'Authorization': `Token ${token}`
      },
    });
    this.jobs = response.data;
  },
};
</script>

<style scoped>
.table-container {
  max-height: 400px; 
  overflow-y: auto;
}

.job-title {
  padding-right: 20px;
}

.submission-date {
  padding-right: 20px; 
}

</style>