<template>
  <div class="garden  eerie" ref="abt">
    <div>
      <p ref="jiorn"></p>
      <button @click="get4rmserver">ТЕЕЕЕСТ</button>
      <p ref="karma"></p>
    </div>
  </div>
</template>
<script setup>
import {ref, onMounted, watch} from "vue"

let karma = ref(null)

function get4rmserver() {
  const usrname = sessionStorage.getItem('username')
  if (usrname) {
    const req = new XMLHttpRequest()
    req.open("post", "http://localhost:3000/orderee")
    req.send('hiwdh')
    req.onload = () => {
      console.log('idwdbpiwdwdpwdbw;ddwdwdwd')
      console.log(req.response)
      jiorn.value.textContent = req.response
    }
  } else {
    let pt = document.createElement('p')
    const ptContent = document.createTextNode("Вы не зарегестрированы!");
    pt.appendChild(ptContent)
    karma.value.replaceWith(pt)
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
