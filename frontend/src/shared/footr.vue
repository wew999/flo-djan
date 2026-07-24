<template>
 <footer class="garden" ref="footee">
   <ul class="flex ">
     <li class="w-4/12 m-4">
       <h3 class="text-2xl font-[Arial_Black]">Про нас</h3>
       <p class="text-sm ">"Наш цветочный магазин имеет очень большую историю. Мы ведём нашу деятельность с 1999 года. С тех пор наша сеть развилась до междугороднего уровня, а сами мы стали профессионалами с большимс опытом в своём деле. блаблаблаблабла"</p>
     </li>
     <li class="m-4">
       <h3 class="text-2xl font-[Arial_Black]">Ссылки</h3>
       <ul class="text-sm ">
         <li><a>Главная</a></li>
         <li><a>Ассортимент</a></li>
         <li><a>Сотрудничество</a></li>
       </ul>
     </li>
     <li class="m-4">
       <h3 class="text-2xl font-[Arial_Black]">Контактная информация</h3>
       <ul class="text-sm">
         <li>
           <h4 class="font-[Arial_Black]">Адрес</h4>
           <p>Оренбург, улица Боровского, 67</p>
         </li>
         <li>
           <h4 class="font-[Arial_Black]">Номер</h4>
           <p>+212-85-06</p>
         </li>
         <li>
           <h4 class="font-[Arial_Black]">Почта</h4>
           <p>sweetdreamsaremadeofthis995@gmail.com</p>
         </li>
       </ul>
     </li>
   </ul>
 </footer>
</template>
<script setup>
import { ref, watch, onMounted  } from 'vue'

let footee = ref(null)


onMounted(() => {
  watch(scorn, (newVal) => {
    switch (newVal) {
      case 'garden':
        footee.value.className = 'garden'
        break
      case 'oasis':
        footee.value.className = 'oasis'
        break
      case 'volcano':
        footee.value.className = 'volcano'
        break
      case 'lipstic':
        footee.value.className = 'lipstic'
        break
      case 'poison':
        footee.value.className = 'poison'
        break
    }
  })
})

</script>