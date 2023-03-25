<script setup lang="ts">
import { format } from 'date-fns';
</script>

<template>
  <div class="time">
    <h1>Current Time: {{ format(new Date(), 'yyyy-mm-dd hh:mm:ss') }}</h1>
  </div>
</template>

