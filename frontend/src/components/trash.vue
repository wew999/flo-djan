<template>
  <div class="garden  eerie" ref="abt">
    <div ref="pipis">
      <p ref="jiorn"></p>
      <p ref="karma"></p>
    </div>
  </div>
</template>
<script setup>
import {ref, onMounted, watch} from "vue"

let karma = ref(null)
let pipis = ref(null)

function rusificate(value) {
  switch (value) {
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
}

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

const jwrpeq2 = new XMLHttpRequest()
jwrpeq2.open("POST", "http://127.0.0.1:8000/postorder/")
const mmsg2 = {special:"getorders"}
const mmd2 = JSON.stringify(mmsg2)
jwrpeq2.withCredentials = true;
jwrpeq2.setRequestHeader('Content-Type', 'application/json');
jwrpeq2.send(mmd2)
jwrpeq2.onload = () => {
  console.log(jwrpeq2.response)
  if (jwrpeq2.response != "Nothing") {
    const ordDatar = JSON.parse(jwrpeq2.response)
    console.log(ordDatar)
    const origDiv = document.createElement('div')
    for (const [key, value] of Object.entries(ordDatar)) {
      let ddiv = document.createElement('div')
      let hd = document.createElement('h1')
      const hdngContent = document.createTextNode(key);
      let para = document.createElement('p')
      const paraContent = document.createTextNode(`Количество: ${value}`);
      hd.className = "text-2xl"
      ddiv.className = "border-b-blue-50 border-2 m-2"

      hd.appendChild(hdngContent)
      para.appendChild(paraContent)
      ddiv.appendChild(hd)
      ddiv.appendChild(para)
      origDiv.appendChild(ddiv)
    }
    origDiv.className = 'center'
    pipis.value.append(origDiv)
  } else {
    jiorn.value.textContent = "Здесь пока ничего нет! Перейдите в раздел 'Ассортимент', чтобы сделать заказ!"
  }
  }





let abt = ref(null)
let jiorn = ref(null)
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
