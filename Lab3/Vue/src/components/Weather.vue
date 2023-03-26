<script setup lang="ts">
import axios from 'axios';
import { API_Key } from '../assets/weatherAPI.vue';

const getWeatherData = async () =>
{
  const url = `https://api.openweathermap.org/data/2.5/weather?q=Paris,on,ca&units=metric&appid=${API_Key}`;

  try 
  { 
    const response = await axios.get(url) 
    const city = response.data.name;
    const temp = response.data.main.temp;
    return {'city': city, 'temp': temp};
  } 
  catch (error) { console.log('ERR: ', error)}
};

  const data = await getWeatherData();
</script>

<template>
  <div class="weather">
    <h1>Weather in {{ data?.city }}: {{ data?.temp }} &#8451;</h1>
  </div>
</template>

<style scoped>
  .weather {
    text-align: center;
  }
</style>