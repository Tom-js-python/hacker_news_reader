<script setup>
const emit = defineEmits(['toggle'])
import { ref } from 'vue'

const dataLoaded = ref(false)

// Information about links to send to API
const numLinks = ref(5)
const numPages = ref(15)
const searchTerm = ref('')
const minPoints = ref(400)

function loadData() {
  dataLoaded.value = !dataLoaded.value
  emit('toggle', {
    dataLoaded: dataLoaded.value,
    numLinks: numLinks.value,
    numPages: numPages.value,
    searchTerm: searchTerm.value,
    minPoints: minPoints.value
  })
}
</script>

<template>
  <p>
    Get the top <input v-model="numLinks" /> links from the first <input v-model="numPages" /> pages
    of the Hacker News Site which have a minimum number of points of <input v-model="minPoints" />
  </p>
  <p>
    Ensure they contain this search term:
    <input v-model="searchTerm" class="search-term" />. Leave blank for no search term.
  </p>
  <button @click="loadData">{{ dataLoaded ? 'Reset Data' : 'Load Data' }}</button>
</template>

<style scoped>
.search-term {
  width: 10rem;
}
button {
  text-align: center;
  margin: 1em auto;
  display: flex;
  padding: 1rem;
  appearance: none;
  background-color: #fafbfc;
  border: 1px solid rgba(27, 31, 35, 0.15);
  border-radius: 6px;
  box-shadow:
    rgba(27, 31, 35, 0.04) 0 1px 0,
    rgba(255, 255, 255, 0.25) 0 1px 0 inset;
  box-sizing: border-box;
  color: #24292e;
  cursor: pointer;
  font-family: -apple-system, system-ui, 'Segoe UI', Helvetica, Arial, sans-serif,
    'Apple Color Emoji', 'Segoe UI Emoji';
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  padding: 6px 16px;
  position: relative;
  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;
  word-wrap: break-word;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

button:hover {
  background-color: #f3f4f6;
  text-decoration: none;
  transition-duration: 0.1s;
}

button:disabled {
  background-color: #fafbfc;
  border-color: rgba(27, 31, 35, 0.15);
  color: #959da5;
  cursor: default;
}

button:active {
  background-color: #edeff2;
  box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
  transition: none 0s;
}
button:focus {
  outline: 1px transparent;
}

input {
  width: 2.5rem;
  background-color: #fafbfc;
  border: 1px solid rgba(27, 31, 35, 0.15);
  border-radius: 4px;
  box-shadow:
    rgba(27, 31, 35, 0.04) 0 1px 0,
    rgba(255, 255, 255, 0.25) 0 1px 0 inset;
  color: #24292e;
  cursor: pointer;
  font-family: -apple-system, system-ui, 'Segoe UI', Helvetica, Arial, sans-serif,
    'Apple Color Emoji', 'Segoe UI Emoji';
  font-size: 14px;
  font-weight: 500;
  padding: 0.2rem;
  position: relative;
  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
}
input:hover {
  background-color: #f3f4f6;
  text-decoration: none;
  transition-duration: 0.1s;
}

input:disabled {
  background-color: #fafbfc;
  border-color: rgba(27, 31, 35, 0.15);
  color: #959da5;
  cursor: default;
}

input:active {
  background-color: #edeff2;
  box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
  transition: none 0s;
}
input:focus {
  outline: 1px transparent;
}
p {
  text-align: left;
  margin: 0.5rem 0;
}
</style>
