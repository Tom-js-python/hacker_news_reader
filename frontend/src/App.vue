<script setup>
import TheMenuBar from './components/TheMenuBar.vue'
import TheLinksTable from './components/TheLinksTable.vue'
</script>

<template>
  <header>Hacker News Web Scraper</header>

  <main>
    <TheMenuBar />
    <TheLinksTable />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}
</style>
