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

<style scoped>
  header {
    background-color: #333;
    padding: 10px;
    text-align: center;
  }
  nav {
    display: flex;
    justify-content: space-around;
  }
  nav a {
    color: #fff;
    text-decoration: none;
  }
  nav a:hover {
    color: #ccc;
  }
</style>