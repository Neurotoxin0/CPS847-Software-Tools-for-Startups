<script setup lang="ts">
  import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/service">Our Services</RouterLink>
      <RouterLink to="/customer">Our Customers</RouterLink>
      <RouterLink to="/about">About Us</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>