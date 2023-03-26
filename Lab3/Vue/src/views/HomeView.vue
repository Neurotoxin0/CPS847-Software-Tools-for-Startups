<script setup lang="ts">
  import Time from '../components/Time.vue'
  import Weather from '../components/Weather.vue'
</script>

<template>
  <div class="home">
    <Time />
    
    <Suspense>
      <Weather />
      <template #fallback, class="loading_message" >Loading...</template>
    </Suspense>
  </div>
</template>

<style scoped>
  .loading_message {
    text-align: center;
  }
</style>