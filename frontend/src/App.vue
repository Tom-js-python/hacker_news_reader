<script setup>
import TheMenuBar from './components/TheMenuBar.vue'
import TheLinksTable from './components/TheLinksTable.vue'
import { ref } from 'vue'

const API_URL = 'http://127.0.0.1:5000/test'
const data_message = ref('No Links Are Loaded')

async function onToggle(isLoaded) {
  data_message.value = 'Scraping Hacker News Site...'
  if (isLoaded) {
    let raw_data = await fetch(API_URL)
    let data = await raw_data.json()
    data_message.value = data.Message
  } else {
    data_message.value = 'No Links Are Loaded'
  }
}
</script>

<template>
  <header>Hacker News Web Scraper</header>

  <main>
    <TheMenuBar @toggle="onToggle" />
    <TheLinksTable :data-message="data_message" />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}
</style>
