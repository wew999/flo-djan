<template>
  <div class="center garden " ref="spids">
<div class=" font-[Arial] ">
  <h1 class="text-center size-12 text-4xl text-nowrap font-bold font-[Arial_Black]">О нас</h1>
  <h2 class=" text-center size-8 text-2xl text-nowrap font-bold font-[Arial_Black]">История</h2>
    <p>Наш цветочный магазин имеет очень большую историю. Мы ведём нашу деятельность с 1999 года. С тех пор наша сеть развилась до междугороднего уровня, а сами мы стали профессионалами с большим опытом в своём деле. блаблаблаблабла</p>
  <h2 class=" text-center size-10 text-2xl text-nowrap font-bold font-[Arial_Black]">Наши цели</h2>
  <ul class="list-disc pl-5">
    <li>Создать удобный сервис, который обеспечит наих клиентов комфортом и удобствами</li>
    <li>Создать огромную сеть цветочных магазинов</li>
    <li>Увеличить качество и доступный ассортимент</li>
    <li>Дарить счастье и радость людям!</li>
  </ul>
  <h2 class=" text-center size-16 text-2xl text-nowrap font-bold font-[Arial_Black]">Наша команда</h2>
    <div class="flex">
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
  <h2 class=" text-center size-16 text-2xl text-nowrap font-bold font-[Arial_Black]">Присоединяйтесь!</h2>
  <p>Хотите стать частью команды? Мы с радостью вас примем! Оставьте заявку и мы свяжемся с вами!</p>
  <button>Оставить заявку</button>
  <h3 class=" text-center size-8 text-1xl text-nowrap font-bold font-[Arial_Black]">Подпишитесь на нашу рассылку</h3>
  <button>Получать рассылку</button>
</div>
  </div>
</template>
<script setup>
import { ref, watch, onMounted  } from 'vue'

let spids = ref(null)

onMounted(() => {
  spids.value.className = `${scorn.value} eerie`
  watch(scorn, (newVal) => {
    switch (newVal) {
      case 'garden':
        spids.value.className = 'garden eerie'
        break
      case 'oasis':
        spids.value.className = 'oasis eerie'
        break
      case 'volcano':
        spids.value.className = 'volcano eerie'
        break
      case 'lipstic':
        spids.value.className = 'lipstic eerie'
        break
      case 'poison':
        spids.value.className = 'poison eerie'
        break
    }
  })
})
</script>