<template>
  <div class="garden  eerie" ref="abt">
    <div ref="pipis">
      <p ref="jiorn"></p>
      <p ref="karma"></p>
    </div>
  </div>
</template>
<script setup lang="jsx">
import {ref, onMounted, watch, h, render} from "vue"

let karma = ref(null)
let pipis = ref(null)
let order =ref({})


async function getOrderImages(point) {
  return new Promise((resolve, reject) => {
    const jwrpeq = new XMLHttpRequest()
    jwrpeq.open("POST", "http://127.0.0.1:8000/producttape/")
    const mmsg = {special: point}
    const mmd = JSON.stringify(mmsg)
    jwrpeq.withCredentials = true;
    jwrpeq.setRequestHeader('Content-Type', 'application/json');
    jwrpeq.send(mmd)
    console.log(point)
    jwrpeq.onload = () => {
      console.log(jwrpeq.response)
      const morroj = JSON.parse(jwrpeq.response)
      resolve(morroj)
    }
  })
}

async function shortage(point) {
  try {
   if (point.length >= 14) {
     return point.slice(0, 12) + '…';
   } else {
     return point
   }
  } catch (error) {
    console.error(error)
  }
}

async function countPrice(price, amount) {
  try {
    const endPrice = price * amount
    return endPrice
  } catch (error) {
    console.error(error)
  }
}

async function processImages(point) {
  try {
    const result = await getOrderImages(point)
    console.log(result)  // ← Здесь будет ваш результат
    return result
  } catch (error) {
    console.error(error)
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

function paymentredirect() {
  window.location.replace('https://localhost:5173/#/pay')
}
let banList = []
let pipsgit = ref({})
let kirta = 0
function wow(commando) {
const jwrpeq2 = new XMLHttpRequest()
jwrpeq2.open("POST", "http://127.0.0.1:8000/postorder/")
const mmsg2 = {special:"getorders"}
const mmd2 = JSON.stringify(mmsg2)
jwrpeq2.withCredentials = true;
jwrpeq2.setRequestHeader('Content-Type', 'application/json');
jwrpeq2.send(mmd2)
jwrpeq2.onload = () => {
  console.log(jwrpeq2.response)
  if (jwrpeq2.response != "Nothing" && jwrpeq2.response != "{}") {
    const ordDatar = JSON.parse(jwrpeq2.response)
    console.log(ordDatar)
    const origDiv = document.createElement('div')
    origDiv.id = "yomama"
    let IDQuantyfier = 0
    for (const [key, value] of Object.entries(ordDatar)) {
      if (value != "0") {
        IDQuantyfier++
        console.log(shortage(key))
        const orderPoint = h(
            "div", {className:"flex center m-1"}, [
              h("div",  [
                h("h1", {id:`${key}67`, className:"w-50 text-2xl center nowrap"}, key),
                h( "img", { id:key, className:"w-50"}),
                h( "p", { className:"center price"}, value),
                h( "p", { id:`${key}76`, className:"center trueprice"} ),
                h('button', { className:"flex justify-center items-center"},  "Изменить")
              ])
            ]
        )
        const larpDiv = document.createElement('div')
        larpDiv.className = "flex center items-center justify-center"
        render(orderPoint, larpDiv )
        origDiv.appendChild(larpDiv)
        let pain = processImages(key).then(result => {

          console.log(result.sourse)
          let superQ = 0
          while (superQ != IDQuantyfier) {
            try {
              superQ++
              console.log(banList)
              document.getElementById(key).src = result.sourse
            } catch (err) {
              console.log(err)
              console.log(superQ)
              console.log(document.getElementById(superQ).src)
              superQ++
            }
            try {
              shortage(key).then(
                  result => {
                    document.getElementById(`${key}67`).innerText = result
                  }
              )
            } catch (err) {
              console.log(err)
            }
          }
          let amounts = document.getElementsByClassName('price')
          for (let amount of amounts ) {
            console.log(amount)
            if (!(amount.innerText.includes(" штук"))) {
              amount.innerText += " штук"}
          }
          let prices = document.getElementsByClassName('trueprice')
          for (let price of prices ) {
            console.log(price)
            if (price.innerText == '' && price.id == `${key}76`) {
              countPrice(result.price, value).then(result => {
                price.innerText = result
                price.innerText += " р."
              })
            }
          }}
        )
      }
    }
    let butDiv = h(
        "div", {className: 'block'}, [
            h("button", {className: 'block', onClick(event) {paymentredirect()}}, "Заказ")
        ]
    )
    render(butDiv, origDiv)
    origDiv.className = 'center'

    if (commando == 'append') {
      pipis.value.append(origDiv)
    } else {
     document.getElementById('yomama').replaceWith(origDiv)
    }
  } else if (jwrpeq2.response == "{}") {
    const jwrpeq3 = new XMLHttpRequest()
    jwrpeq3.open("POST", "http://127.0.0.1:8000/postorder/")
    const mmsg3 = {special:"returnorder"}
    const mmd3 = JSON.stringify(mmsg3)
    jwrpeq3.withCredentials = true;
    jwrpeq3.setRequestHeader('Content-Type', 'application/json');
    jwrpeq3.send(mmd3)
    jwrpeq3.onload = () => {
      const ordDatar = JSON.parse(jwrpeq3.response)
      console.log(ordDatar)
      const origDiv = document.createElement('div')
      for (const [key, value] of Object.entries(ordDatar)) {
        pipsgit.value[key] = value
        let ddiv = document.createElement('div')
        let hd = document.createElement('h1')
      //  let pict = <img src={imagificate(key)}>
        pict.src = imagificate(key)
        pict.className = "w-50"
        const hdngContent = document.createTextNode(rusificate(key));
        let para = document.createElement('p')
        const paraContent = document.createTextNode(`Количество: ${value}`);
        hd.className = "text-2xl"
        ddiv.className = "border-b-blue-50 border-2 m-2"
        let butt2 = document.createElement('button')
        const butt2Content = document.createTextNode('+');
        butt2.appendChild(butt2Content)
        let butt3 = document.createElement('button')
        butt2.id = key
        butt3.id = key

        const butt3Content = document.createTextNode('-');
        hd.appendChild(hdngContent)
        butt3.appendChild(butt3Content)
        butt2.addEventListener('click', add2cart)
        butt3.addEventListener('click', rem4rmcart)
        hd.appendChild(hdngContent)
        para.appendChild(paraContent)
        ddiv.appendChild(pict)
        ddiv.appendChild(hd)
        ddiv.appendChild(para)
        ddiv.appendChild(butt3)
        ddiv.appendChild(butt2)
        origDiv.appendChild(ddiv)
    }
      origDiv.className = 'center'
      pipis.value.append(origDiv)
    }
  } else {
    jiorn.value.textContent = "Здесь пока ничего нет! Перейдите в раздел 'Ассортимент', чтобы сделать заказ!"
  }
  }
  console.log(pipsgit.value)}


wow('append')


  function add2cart(event) {
    kirta = pipsgit.value[event.target.id]
    kirta++
    pipsgit.value[event.target.id] = kirta
    console.log(pipsgit.value)
  }
  function rem4rmcart(event) {
    kirta = pipsgit.value[event.target.id]
    if(kirta >0) {
      kirta--
      pipsgit.value[event.target.id] = kirta
      console.log(pipsgit.value)
    }
  }


function send2server() {
  // const usrname = sessionStorage.getItem('username')
  //console.log(usrname)
  //if (usrname) {
  const req = new XMLHttpRequest()
  req.open("POST", "http://127.0.0.1:8000/postorder/")
  const yepy = JSON.stringify(pipsgit.value)
  console.log(`${order.value} ===== ${yepy}`)
  req.withCredentials = true;
  req.setRequestHeader('Content-Type', 'application/json');
  req.send(yepy)
  req.onload = () => {
    console.log("$")
    wow('replace')
  }}



let abt = ref(null)
let jiorn = ref(null)
onMounted(() => {
  watch(pipsgit.value, (newVal) => {
    console.log(pipsgit.value)
    send2server()
    console.log(pipsgit.value)
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
