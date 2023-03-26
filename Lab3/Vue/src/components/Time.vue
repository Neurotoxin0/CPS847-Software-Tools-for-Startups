<script setup lang="ts">
import { format } from 'date-fns';
</script>

<template>
  <div class="time">
    <h1>Current Time: {{ format(new Date(), 'yyyy-MM-dd HH:mm:ss') }}</h1>
  </div>
</template>

<style scoped>
  .time {
    text-align: center;
  }
</style>
