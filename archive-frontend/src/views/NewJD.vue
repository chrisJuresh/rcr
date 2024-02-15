<template>
  <div>
    <h2>Submit New JD</h2>
    <form @submit.prevent="submitJD" class="form-grid">
      <div class="form-item">
        <label for="document">JD Document:</label>
        <input type="file" id="document" @change="handleFileUpload" required>
      </div>
      <div class="form-item">
        <label>Consultant Type:</label>
        <div>
          <input type="radio" id="radiologist" value="RADIOLOGY" v-model="selectedConsultantType">
          <label for="radiologist">Consultant Radiologist</label>
          <input type="radio" id="oncologist" value="ONCOLOGY" v-model="selectedConsultantType">
          <label for="oncologist">Consultant Oncologist</label>
        </div>
      </div>
      <div class="specialities">
        <div class="speciality-item">
          <label for="primary-specialities">Primary Specialities:</label>
          <select id="primary-specialities" v-model="selectedPrimaryspecialities" multiple>
            <option v-for="speciality in filteredspecialities" :key="speciality.id" :value="speciality.id">
              {{ speciality.name }}
            </option>
          </select>
        </div>
        <div class="speciality-item">
          <label for="secondary-specialities">Sub Specialities:</label>
          <select id="secondary-specialities" v-model="selectedSecondaryspecialities" multiple>
            <option v-for="speciality in filteredspecialities" :key="speciality.id" :value="speciality.id">
              {{ speciality.name }}
            </option>
          </select>
        </div>
      </div>
      <button type="submit" class="form-item" :disabled="selectedPrimaryspecialities.length === 0">Submit</button>
    </form>
    <router-link to="/panel">Go to Panel</router-link>
    <div v-if="feedbackMessage">{{ feedbackMessage }}</div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

const specialities = ref([]);
const selectedPrimaryspecialities = ref([]);
const selectedSecondaryspecialities = ref([]);
const selectedConsultantType = ref('RADIOLOGY'); 
const userTrust = ref(null);

// Fetch user's trust on mounted
onMounted(async () => {
  try {
    const token = localStorage.getItem('token');
    const profileResponse = await axios.get('http://localhost:8000/profile/', {
      headers: {
        'Authorization': `Token ${token}`
      },
    });
    userTrust.value = profileResponse.data.trust; 

    const specialitiesResponse = await axios.get('http://localhost:8000/specialities/', {
      headers: {
        'Authorization': `Token ${token}`
      },
    });
    specialities.value = specialitiesResponse.data;
  } catch (error) {
    console.error(error);
  }
});

const filteredspecialities = computed(() => {
  const filtered = specialities.value.filter(speciality => speciality.consultant_type_name === selectedConsultantType.value);
  return filtered;
});

const file = ref(null);
const feedbackMessage = ref('');

function handleFileUpload(event) {
  file.value = event.target.files[0];
}

async function submitJD() {
  if (!file.value) {
    feedbackMessage.value = 'Please select a file to upload.';
    return;
  }

  const formData = new FormData();
  formData.append('document', file.value);
  formData.append('trust', userTrust.value);
  formData.append('consultantType', selectedConsultantType.value);
  
  selectedPrimaryspecialities.value.forEach(id => {
    formData.append('primarySpecialities', id);
  });
  selectedSecondaryspecialities.value.forEach(id => {
    formData.append('subSpecialities', id);
  });

  const token = localStorage.getItem('token');
  try {
    const response = await axios.post('http://localhost:8000/jds/', formData, {
      headers: {
        'Authorization': `Token ${token}`,
        'Content-Type': 'multipart/form-data', // Ensure correct content type
      },
    });
    feedbackMessage.value = 'JD submitted successfully!';
    console.log(response.data); 
  } catch (error) {
    feedbackMessage.value = error.response.data.detail || 'An error occurred while submitting the JD.';
    console.error(error);
  }
}
</script>

<style scoped>
</style>