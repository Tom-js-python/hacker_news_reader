<script setup>
const props = defineProps({
  dataMessage: String,
  newsLinks: Object
})
</script>

<template>
  <p v-if="dataMessage != 'Loaded'">{{ dataMessage }}</p>
  <table v-if="dataMessage == 'Loaded'" class="styled-table">
    <thead>
      <tr>
        <td>Points</td>
        <td>Article</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="newsLink in newsLinks">
        <td>{{ newsLink.points }}</td>
        <td>
          <a :href="newsLink.link" target="_blank">{{ newsLink.title }}</a>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.styled-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.styled-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}
.styled-table th,
.styled-table td {
  text-align: left;
  padding: 12px 15px;
}
.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}
</style>
