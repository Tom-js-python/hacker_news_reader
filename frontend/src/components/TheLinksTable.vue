<script setup>
const props = defineProps({
  dataLoaded: Boolean
})
</script>

<template>
  <p>{{ dataLoaded ? 'Data Loaded!' : 'Data Not Loaded' }}</p>
</template>
