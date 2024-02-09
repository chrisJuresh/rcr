<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th class="id">Reference</th>
          <th class="Consultant">Consultant</th>
          <th class="submission-date">Submission Date</th>
          <th class="consultation-type">Primary Specialities</th>
          <th class="speciality">Sub Specialities</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="jd in jd" :key="jd.id">
          <td class="id">{{ jd.id }}</td>
          <td class="jd-title">{{ jd.consultantType }}</td>
          <td class="submission-date">{{ formatDate(jd.submission_date) }}</td>
          <td class="consultant-type">{{ jd.primarySpecialities }}</td>
          <td class="speciality">{{ jd.subSpecialities }}</td>
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
      jd: [],
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
    this.jd = response.data;
  },
};
</script>

<style scoped>
.table-container {
  max-height: 400px; 
  overflow-y: auto;
}

.jd-title {
  padding-right: 20px;
}

.submission-date {
  padding-right: 20px; 
}

</style>