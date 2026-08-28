<script setup lang="jsx">
import {onMounted, ref, watch, h, render} from "vue";

function displayProduction() {
  const jwrpeq = new XMLHttpRequest()
  jwrpeq.open("GET", "http://127.0.0.1:8000/producttape")
  jwrpeq.withCredentials = true;
  jwrpeq.send(null)
  jwrpeq.onload = () => {
    if (jwrpeq.response == "Nothing") {
      messageWindow.value.innerText = "Пока что здесь нет ни одного товара!"
    }
    else {
      console.log(jwrpeq.response)
    }
  }
}




const jwrpeq = new XMLHttpRequest()
jwrpeq.open("POST", "http://127.0.0.1:8000/productbase/")
const mmsg = {special:"redirect"}
const mmd = JSON.stringify(mmsg)
jwrpeq.withCredentials = true;
jwrpeq.setRequestHeader('Content-Type', 'application/json');
jwrpeq.send(mmd)
jwrpeq.onload = () => {
  console.log(jwrpeq.response)
  if (jwrpeq.response === "REDIRTOLOGIN") {
    window.location.replace('https://localhost:5173/#/login')
  } else if (jwrpeq.response === "NOT ALLOWED") {
    window.location.replace('https://localhost:5173/#/')
  } else {
    displayProduction()
  }
}
//const count = ref(0)
//onst double = computed(() => count.value * 2)
///function increment() {
//  count.value++
//}

const dbContent = ref(null)
const messageWindow = ref(null)
const appendbutton = ref(null)
const newDiv = ref(null)
const abt = ref(null)





let numr = 0
function newProduct() {
  const vnode = h(
      'div', // type
      {  }, // props
      [ h(
          'div', Array.from({ length: 3 }).map(() => {
            return h('input', {id: `inp${numr++}`, class: "block"})
          })
      ),
        h("button",
            {
              onClick(event) {
                saveProduct()
              }
            },
            "Добавить"
          )
      ]
  )
  function saveProduct() {
    const req = new XMLHttpRequest()
    req.open("POST", "http://127.0.0.1:8000/producttape/")
    req.withCredentials = true;
    req.setRequestHeader('Content-Type', 'application/json');
    const hdng = document.getElementById("inp0")
    const src = document.getElementById("inp1")
    const prc = document.getElementById("inp2")
    const cooljsonobject = JSON.stringify({heading: hdng.value, info: src.value, prc: prc.value})
    console.log(cooljsonobject)
    req.send(cooljsonobject)
    req.onload = () => {
      console.log(req.response)
    }
  }
  console.log(newDiv.value)
  render(vnode, newDiv.value);
  const button = document.getElementById('joma')
 // button.addEventListener('click', saveProduct)
  console.log("OWHDS")
  const hdng = document.getElementById("inp0")
  const src = document.getElementById("inp1")
  const prc = document.getElementById("inp2")
  hdng.placeholder = "Заголовок"
  src.placeholder = "URL картинки (700x700)"
  prc.placeholder = "Цена"
  newDiv.value.className = "block"
  return vnode
}

function preview(event) {
  const prewiewDiv = <div>
    <h2>{headng}</h2>
    <img src={srcc} />
    <div>
      <p>{price}</p>
      <button>В корзину</button>
    </div>
  </div>
}

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
function annihilation() {
  const jwrpeq = new XMLHttpRequest()
  jwrpeq.open("GET", "http://127.0.0.1:8000/dropdb")
  jwrpeq.withCredentials = true;
  jwrpeq.send(null)
  jwrpeq.onload = () => {
    if (jwrpeq.response == "Nothing") {
      messageWindow.value.innerText = "Пока что здесь нет ни одного товара!"
    }
    else {
      console.log(jwrpeq.response)
    }
  }
}
</script>
<template>
  <div ref = "abt">
    <button ref="appendButton" @click="newProduct"> Добавить товар</button>
    <p ref="messageWindow" ></p>
    <button @click="annihilation">Удалить все бд</button>
    <div ref="newDiv">
    </div>
    <div ref="dbContent">
    </div>
  </div>
</template>
