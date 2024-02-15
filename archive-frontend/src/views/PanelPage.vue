<template>
  <div>
    <h1>Panel</h1>
    <JobDescriptionsList />
  </div>
</template>

<script>
import JobDescriptionsList from '../components/JD.vue';

export default {
  name: 'PanelPage',
  components: {
    JobDescriptionsList,
  },
};
</script>