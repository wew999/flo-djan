<script setup>
import maini from './components/maini.vue'
import footr from './shared/footr.vue'
import Navb from "./shared/navb.vue";
import login from './components/login.vue'
import about from './components/about.vue'
import assortiment from './components/assortiment.vue'
import loadproduction from './components/loadproduction.vue'
import pay from './components/pay.vue'
import trash from './components/trash.vue'
import {ref, computed} from 'vue'



const routes = {
  '/': maini,
  '/trash': trash,
  '/assortiment': assortiment,
  '/login': login,
  '/pay': pay,
  '/loadproduction': loadproduction
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/']
})
</script>
<template>
  <navb />
  <!-- <li><a href="#/">Главная</a></li>
   <li><a href="#/about">Ассортимент</a></li> -->
   <component :is="currentView" />
   <footr />
 </template>
