<template>
  <div class="garden eerie" ref="abt">
    <div class="center">
      <div class=' h-[80vh] bg-no-repeat font-[Arial_Black] border-b-blue-50 border-4' style="background-image: url('https://avatars.mds.yandex.net/i?id=cf9c77a61ce621b7d08a7387394339cf_l-5282568-images-thumbs&n=13')";>
        <h1 class="text-6xl">Цветочный магазин</h1>
        <p class="text-2xl">Наша сеть цветочных магазинов - отличный способ
          порадовать и поздравить ваших родных и близких.</p>
        <button class="text-2xl"> Перейти к ассортименту</button>
      </div>
    </div>
    <div class="text-center">
    <h1 class="font-[Arial_Black] text-4xl">Про нас</h1>
    <p class="text-2xl">Мы - широкая междугородняя сеть цветочных магазинов. Наше основное преемущество перед конкурентами - широкий ассортимент товаров. Заинтресованы?</p>
    <button>Узнайте больше!</button>
    <h1>Примеры наших товаров:</h1>
    <div class="flex center">
      <div>
        <img class="w-32" src="https://a1.drive-data.ru/MveNo3I81Y8H_L2MGDVJwH6rOaI-1920.jpg">
      </div>
      <div>
        <img class="w-32" src="https://a1.drive-data.ru/MveNo3I81Y8H_L2MGDVJwH6rOaI-1920.jpg">
      </div>
      <div>
        <img class="w-32" src="https://a1.drive-data.ru/MveNo3I81Y8H_L2MGDVJwH6rOaI-1920.jpg">
      </div>
      <div>
        <img class="w-32" src="https://a1.drive-data.ru/MveNo3I81Y8H_L2MGDVJwH6rOaI-1920.jpg">
      </div>
    </div>
    </div>
  </div>
</template>
<script setup>
import { ref, watch, onMounted  } from 'vue'
import {themeMemory} from "../composables/themec.js";

let abt = ref(null)
onMounted(() => {
  abt.value.className = `${scorn.value} eerie`
  watch(scorn, (newVal) => {
    switch (newVal) {
      case 'garden':
        abt.value.className = 'garden eerie'
        break
      case 'oasis':
        abt.value.className = 'oasis eerie'
        break
      case 'volcano':
        abt.value.className = 'volcano eerie'
        break
      case 'lipstic':
        abt.value.className = 'lipstic eerie'
        break
      case 'poison':
        abt.value.className = 'poison eerie'
        break
    }
  })
})
</script>
