<script setup>
const emit = defineEmits(['toggle'])
import { ref } from 'vue'

const dataLoaded = ref(false)

function loadData() {
  dataLoaded.value = !dataLoaded.value
  emit('toggle', dataLoaded.value)
}
</script>

<template>
  <button @click="loadData">{{ dataLoaded ? 'Reset Data' : 'Load Data' }}</button>
</template>

<style scoped>
button {
  display: inline;
  margin-bottom: 1em;
}
</style>
