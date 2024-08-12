<script setup>
import TheMenuBar from './components/TheMenuBar.vue'
import TheLinksTable from './components/TheLinksTable.vue'
import { ref } from 'vue'

const dataLoaded = ref(false)

function onToggle(isLoaded) {
  dataLoaded.value = isLoaded
}
</script>

<template>
  <header>Hacker News Web Scraper</header>

  <main>
    <TheMenuBar @toggle="onToggle" />
    <TheLinksTable :data-loaded="dataLoaded" />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}
</style>
