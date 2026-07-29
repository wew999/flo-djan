<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <nav class="garden h-10" ref="nnn">
    <ul class="flex justify-around font-[Arial]" >
      <li>
        <div class="flex w-2xl">
          <img src="https://cdn-icons-png.flaticon.com/512/5515/5515950.png" class=" size-8">
          <h1 class="size-16 text-2xl text-nowrap font-bold font-[Arial_Black]">Магазин цветочков</h1>
        </div>
      </li>
      <li><a href="#/">Главная</a></li>
      <li><a href="#/assortiment">Ассортимент</a></li>
      <li><a href="#/trash">Корзина</a></li>
      <log />
      <li>
        <label for="referrer">
        <select id="referrer" name="referrer" class="w-16" v-model="selected">
          <option value="" >Тема</option>
          <option value="1" @click="blackTheme" class="garden"></option>
          <option value="2" @click="orangeTheme" class="oasis"></option>
          <option value="3" @click="blueTheme" class="volcano"></option>
          <option value="4" @click="pinkTheme" class="lipstic"></option>
          <option value="5" @click="limeTheme" class="poison"></option>
        </select>
      </label>
      </li>
    </ul>
  </nav>
</template>
<script setup>
import Log from "./log.vue";

console.log("NAV IS WORKING")
import { ref, watch, onMounted } from 'vue'
let nnn = ref(null)
console.log(nnn)

function blackTheme() {
  document.cookie="theme=garden"
}
function orangeTheme() {
  document.cookie="theme=oasis"
}
function blueTheme() {
  document.cookie="theme=volcano"
}
function pinkTheme() {
  document.cookie="theme=lipstic"
}
function limeTheme() {
  document.cookie="theme=poison"
}
let selected = ref('')

watch(selected, (newVal, oldVal) => {
  switch (newVal) {
    case '1':
      blackTheme()
      console.log(document.cookie)
      break
    case '2':
      orangeTheme()
      console.log(document.cookie)
      break
    case '3':
      blueTheme()
      console.log(document.cookie)
      break
    case '4':
      pinkTheme()
      console.log(document.cookie)
      break
    case '5':
      limeTheme()
      console.log(document.cookie)
      break
  }
});
import {themeMemory} from "../composables/themec.js";

onMounted(() => {
  themeMemory()
  scorn.value = 'chirp'
  scorn.value = 'garden'
  watch(scorn, (newVal, oldVal) => {
    switch (newVal) {
      case 'garden':
        nnn.value.className = 'garden'
        break
      case 'oasis':
        nnn.value.className = 'oasis'
        break
      case 'volcano':
        nnn.value.className = 'volcano'
        break
      case 'poison':
        nnn.value.className = 'poison'
        break
      case 'lipstic':
        nnn.value.className = 'lipstic'
        break
    }
  });})

</script>

