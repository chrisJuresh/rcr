<template>
  <div>
    <h2>Submit New JD</h2>
    <form @submit.prevent="submitJD">
      <div>
        <label for="document">JD Document:</label>
        <input type="file" id="document" @change="handleFileUpload" required>
      </div>
      <button type="submit">Submit</button>
    </form>
  <router-link to="/panel">Go to Panel</router-link>
    <div v-if="feedbackMessage">{{ feedbackMessage }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

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

    
const token = localStorage.getItem('token');
  try {
    const response = await axios.post('http://localhost:8000/jds/', formData, {
      headers: {
        'Authorization': `Token ${token}`
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