<template>
  <div class="garden eerie" ref="abt">
    <div class="text-center center flex">
      <figure>
        <img src="https://www.roza4u.ru/image/cache/catalog/15_roz_Red_Monster_/15_roz_Red_Monster_1-700x700.jpg">
        <h2>Букет роз ред монстр</h2>
        <figcaption>500 р.</figcaption>
        <button class="orden" id="monstr">Заказать</button>
      </figure>
      <figure>
        <img src="https://www.roza4u.ru/image/cache/catalog/15_roz_Red_Monster_/15_roz_Red_Monster_1-700x700.jpg">
        <h2>Букет роз ред монстр</h2>
        <figcaption>500 р.</figcaption>
        <button class="orden" id="monstr1">Заказать</button>
      </figure>
      <figure>
        <img src="https://www.roza4u.ru/image/cache/catalog/15_roz_Red_Monster_/15_roz_Red_Monster_1-700x700.jpg">
        <h2>Букет роз ред монстр</h2>
        <figcaption>500 р.</figcaption>
        <button class="orden" id="monstr2">Заказать</button>
      </figure>
      <figure>
        <img src="https://www.roza4u.ru/image/cache/catalog/15_roz_Red_Monster_/15_roz_Red_Monster_1-700x700.jpg">
        <h2>Букет роз ред монстр</h2>
        <figcaption>500 р.</figcaption>
        <button class="orden" id="monstr3">Заказать</button>
      </figure>
      <figure>
        <img src="https://www.roza4u.ru/image/cache/catalog/15_roz_Red_Monster_/15_roz_Red_Monster_1-700x700.jpg">
        <h2>Букет роз ред монстр</h2>
        <figcaption>500 р.</figcaption>
        <button class="orden" id="monstr4">Заказать</button>
      </figure>
    </div>
    <button class="text-2xl" ref="potverd">Подтвердить</button>
    <p ref="karma"></p>
  </div>
</template>
<script setup>
import { ref, watch, onMounted  } from 'vue'
import {themeMemory} from "../composables/themec.js";

const jwrpeq = new XMLHttpRequest()
jwrpeq.open("POST", "http://127.0.0.1:8000/postuser/")
const mmsg = {special:"redirect"}
const mmd = JSON.stringify(mmsg)
jwrpeq.withCredentials = true;
jwrpeq.setRequestHeader('Content-Type', 'application/json');
jwrpeq.send(mmd)
jwrpeq.onload = () => {
  console.log(jwrpeq.response)
  if (jwrpeq.response === "REDIRTOLOGIN") {
    window.location.replace('https://localhost:5173/#/login')
  }}

let abt = ref(null)
let potverd = ref(null)
let karma = ref(null)
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

let order = {}


function changebutton(event) {
  let kirta = 0
  function add2cart(event) {
    kirta++
    order[event.target.id] = kirta
    console.log(order)
  }
  function rem4rmcart(event) {
    if(kirta >0) {
      kirta--
      order[event.target.id] = kirta
      console.log(order)
    }
  }
  kirta++
  order[event.target.id] = kirta
  console.log(order)
  let ddiv = document.createElement('div')
  let butt = document.createElement('button')
  const hdngContent = document.createTextNode("В корзину");
  let butt2 = document.createElement('button')
  const hdngContent2 = document.createTextNode("+");
  let butt3 = document.createElement('button')
  const hdngContent3 = document.createTextNode("-");
  butt.appendChild(hdngContent)
  butt2.appendChild(hdngContent2)
  butt3.appendChild(hdngContent3)
  ddiv.appendChild(butt)
  ddiv.appendChild(butt2)
  ddiv.appendChild(butt3)
  butt2.id = event.target.id
  butt2.addEventListener('click', add2cart)
  butt3.id = event.target.id
  butt3.addEventListener('click', rem4rmcart)
  event.target.replaceWith(ddiv)
}
function send2server() {
 // const usrname = sessionStorage.getItem('username')
  //console.log(usrname)
  //if (usrname) {
    order.username = 'обама'
    const req = new XMLHttpRequest()
    req.open("POST", "http://127.0.0.1:8000/postuser")
    const yepy = JSON.stringify(order)
    console.log(`${order} ===== ${yepy}`)
    req.send(yepy)
    req.onload = () => {
      console.log(req.response)
      if (req.response === "REDIRTOLOGIN") {
        window.location.replace('https://localhost:5173/#/login')
      }
    }
 // } else {
  //    let pt = document.createElement('p')
  //    const ptContent = document.createTextNode("Вы не зарегестрированы!");
   //   pt.appendChild(ptContent)
   //   karma.value.replaceWith(pt)
   // }
}

const orden = document.getElementsByClassName('orden')

onMounted(() => {
  let te = [...orden]

console.log(te)
 for (const ord in te) {
   console.log(te[ord])
   te[ord].addEventListener('click', changebutton)
 }
 potverd.value.addEventListener('click', send2server)
})
</script>
