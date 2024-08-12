<script setup>
import { ref } from 'vue'

const data = ref('Data Not Loaded')

function loadData() {
  data.value = 'Data Loaded!'
}
</script>

<template>
  <button @click="loadData">Load Data</button>
  <p>{{ data }}</p>
</template>

<style scoped>
button {
  display: inline;
  margin-bottom: 1em;
}
</style>
