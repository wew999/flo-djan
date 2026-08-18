<template>
  <div class="garden eerie" ref="abt">
    <div class="text-center center flex" ref="omfg">
    </div>
    <p ref="karma"></p>
    <p ref="messageWindow"></p>
  </div>
</template>
<script setup lang="jsx">
import { ref, watch, onMounted, h, render  } from 'vue'
import {themeMemory} from "../composables/themec.js";

const messageWindow = ref(null)

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
let omfg = ref(null)

let order = ref({})



/////
/*const  shopreq = new XMLHttpRequest()
shopreq.open("POST", "http://127.0.0.1:8000/productbase/")
const shopmmsg = {special:"redirect"}
const shopmmd = JSON.stringify(shopmmsg)
shopreq.withCredentials = true;
shopreq.setRequestHeader('Content-Type', 'application/json');
shopreq.send(shopmmd)
shopreq.onload = () => {
  console.log(shopreq.response)
  if (shopreq.response === "REDIRTOLOGIN") {
    window.location.replace('https://localhost:5173/#/login')
  }} */

function shopcreation(headng, srcc, price) {
  const stateOneTemplate =
      h(
          'div',
          {},
            h("img", {src:srcc}), [h("h2", {}, headng),
          h("div",
              {},
              [h("p", {}, price),
                h("button", {id: headng,
                  onClick(event) {
                    let kirta = 0
                    function add2cart(event) {
                      kirta++
                      order.value[event.target.id] = kirta
                      console.log(order.value)
                      pip.textContent= kirta
                    }
                    function rem4rmcart(event) {
                      if(kirta >0) {
                        kirta--
                        order.value[event.target.id] = kirta
                        console.log(order.value)
                        pip.textContent= kirta
                      }
                    }
                    kirta++
                    order.value[event.target.id] = kirta
                    console.log(order.value)
                    let ddiv = document.createElement('div')
                    let butt2 = document.createElement('button')
                    const hdngContent2 = document.createTextNode("+");
                    let butt3 = document.createElement('button')
                    const hdngContent3 = document.createTextNode("-");
                    let pip = document.createElement('p')
                    pip.textContent= kirta
                    butt2.appendChild(hdngContent2)
                    butt3.appendChild(hdngContent3)
                    ddiv.appendChild(butt3)
                    ddiv.appendChild(pip)
                    ddiv.appendChild(butt2)
                    butt2.id = event.target.id
                    butt2.addEventListener('click', add2cart)
                    butt3.id = event.target.id
                    butt3.addEventListener('click', rem4rmcart)
                    ddiv.className = "flex center"
                    event.target.replaceWith(ddiv)
                  }
                  }, "В корзину")
              ])
          ]
      )
  let ramm = document.createElement("div")
  render(stateOneTemplate, ramm);
  omfg.value.appendChild(ramm)
  ////////////////
}
const marketreq = new XMLHttpRequest()
marketreq.open("GET", "http://127.0.0.1:8000/producttape")
marketreq.withCredentials = true;
marketreq.send(null)
marketreq.onload = () => {
  if (marketreq.response == "Nothing") {
    messageWindow.value.innerText = "Пока что здесь нет ни одного товара!"
  }
  else {
    let market = JSON.parse(marketreq.response)
    for (let ahh of market) {
      console.log(ahh)
      shopcreation(ahh.fields.heading, ahh.fields.info, ahh.fields.price)
    }
    console.log(marketreq.response)
  }
}






function changebutton(event) {
  let kirta = 0
  function add2cart(event) {
    kirta++
    order.value[event.target.id] = kirta
    console.log(order.value)
    pip.textContent= kirta
  }
  function rem4rmcart(event) {
    if(kirta >0) {
      kirta--
      order.value[event.target.id] = kirta
      console.log(order.value)
      pip.textContent= kirta
    }
  }
  kirta++
  order.value[event.target.id] = kirta
  console.log(order.value)
  let ddiv = document.createElement('div')
  let butt2 = document.createElement('button')
  const hdngContent2 = document.createTextNode("+");
  let butt3 = document.createElement('button')
  const hdngContent3 = document.createTextNode("-");
  let pip = document.createElement('p')
  pip.textContent= kirta
  butt2.appendChild(hdngContent2)
  butt3.appendChild(hdngContent3)
  ddiv.appendChild(butt3)
  ddiv.appendChild(pip)
  ddiv.appendChild(butt2)
  butt2.id = event.target.id
  butt2.addEventListener('click', add2cart)
  butt3.id = event.target.id
  butt3.addEventListener('click', rem4rmcart)
  ddiv.className = "flex center"
  event.target.replaceWith(ddiv)
}
function send2server() {
 // const usrname = sessionStorage.getItem('username')
  //console.log(usrname)
  //if (usrname) {
    const req = new XMLHttpRequest()
    req.open("POST", "http://127.0.0.1:8000/postorder/")
    const yepy = JSON.stringify(order.value)
    console.log(`${order.value} ===== ${yepy}`)
    req.withCredentials = true;
    req.setRequestHeader('Content-Type', 'application/json');
    req.send(yepy)
    req.onload = () => {
      console.log(req.response)
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
})

onMounted(() => {
  watch(order.value, (newVal) => {
    send2server()
  })
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
