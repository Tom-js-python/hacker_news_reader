<script setup>
import TheMenuBar from './components/TheMenuBar.vue'
import TheLinksTable from './components/TheLinksTable.vue'
import { ref } from 'vue'

const API_URL = 'http://127.0.0.1:5000/'
const data_message = ref('No Links Are Loaded')
const news_links = ref([])

async function onToggle(formInfo) {
  data_message.value = 'Scraping Hacker News Site...'
  let isLoaded = formInfo.dataLoaded
  let numLinks = formInfo.numLinks
  let numPages = formInfo.numPages
  let searchTerm = formInfo.searchTerm
  let minPoints = formInfo.minPoints
  console.log('numLinks: ' + numLinks)
  console.log('numPages: ' + numPages)
  console.log('searchTerm: ' + searchTerm)
  console.log('minPoints: ' + minPoints)
  if (isLoaded) {
    let raw_data = await fetch(API_URL)
    let data = await raw_data.json()
    data_message.value = 'Loaded'
    news_links.value = data.NewsLinks
  } else {
    data_message.value = 'No Links Are Loaded'
  }
}
</script>

<template>
  <header><h1>Hacker News Web Scraper</h1></header>

  <main>
    <TheMenuBar @toggle="onToggle" />
    <TheLinksTable :data-message="data_message" :news-links="news_links" />
  </main>
</template>

<style scoped>
header {
  text-align: center;
  line-height: 1.5;
  padding-bottom: 2rem;
}
</style>
