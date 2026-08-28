<template>
  <div ref="abt" class=" garden eerie">
    <div id="pips">
      <p ref="jiorn"></p>
    </div>
  </div>
</template>
<script setup lang="jsx">
import {ref, onMounted, watch, h, render} from "vue"

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
let tulup57 = 0

async function countPrice(price, amount) {
  try {
    const endPrice = price * amount
    console.log(price)
    console.log(amount)
    console.log(endPrice)
    tulup57 += endPrice
    console.log(tulup57)
    return {notEnd: endPrice, endEnd: tulup57}
  } catch (error) {
    console.error(error)
  }
}

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

async function processImages(point) {
  try {
    const result = await getOrderImages(point)
    console.log(result)  // ← Здесь будет ваш результат
    return result
  } catch (error) {
    console.error(error)
  }
}


let pipsgit = ref({})
let abt = ref(null)

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
      origDiv.className = 'grid grid-cols-2 gap-4'
      const larperDiv = document.createElement('div')
      larperDiv.className = "flex center items-center justify-center"
      const datarLength =  Object.entries(ordDatar).length
      const orderDatar = ref(Object.entries(ordDatar))
      const date = new Date()
      let coolDate = date.setDate(date.getDate() + 2);
      coolDate = new Date(coolDate)
      coolDate = `${coolDate.getDate()}.${coolDate.getMonth()}.${coolDate.getFullYear()}`
      for (const [key, value] of Object.entries(ordDatar)) {
        if (value != "0") {

        const orderPoint = h(
            "div", {className:"flex center m-1"}, [
              h("div",  [
                h("h1", {id:`${key}67`, className:"w-50 text-2xl center nowrap"}, key),
                h( "img", { id:key, className:"w-50"}),
                h( "p", {id:`${key}76`, className:"center price"}, value),
                h( "p", { className:"center trueprice"}, `Количество : ${value}`),
              ])
            ]
        )
        const larpDiv = document.createElement('div')
        larpDiv.className = "flex center items-center justify-center"
        render(orderPoint, larpDiv )
        larperDiv.appendChild(larpDiv)
        let pain = processImages(key).then( result => {
            document.getElementById(key).src = result.sourse
              shortage(key).then(result =>{

                  document.getElementById(`${key}67`).innerText = result
              })
          console.log(typeof orderDatar.value)
            countPrice(result.price, value).then(result =>{
                const orderMenu = h(
                    "div", {className: "border-2 border-dashed"}, [
                        h(  "div", {className:"center"}, [
                          h( "h1", {className: "center text-4xl font-[Arial_Black] w-1/2"}, `Ваш заказ:`),
                        ]),
                        h(  "div", {className:"center"}, [
                          h( "h1", {className: "center text-3xl font-[Arial_Black] "}, `Итоговая цена: ${result.endEnd}`),
                        ]),
                        h(  "div", {className:"center"}, [
                        h( "ul", {className: "list-disc list-inside   text-1xl"}, orderDatar.value.map((item) => {
                          if (item[1] != "0") {
                            return h('li', { key: item }, `${item[0]}: ${item[1]}`)
                          }
                        })),]),
                        h("p", {className: " text-2xl center"}, "Адрес доставки:", [
                            h("input", {placeholder:"Адрес"})
                        ]),
                        h("p", {className: " text-2xl center"}, `Ориентировочная дата доставки: ${coolDate}`),
                        h(  "div", {className:"center"}, [
                          h("button", {className: " text-2xl center"}, "Оформить заказ")
                        ]),
                    ]
                )
                render(orderMenu, origDiv)
                document.getElementById(`${key}76`).innerText = result.notEnd
                document.getElementById(`${key}76`).innerText += " р."
                })
              }
        )
      }}
      origDiv.appendChild(larperDiv)
      if (commando == 'append') {
        const pips =  document.getElementById('pips')
        console.log(pips)
        pips.className='center flex'
        pips.append(origDiv)
      } else {
        document.getElementById('yomama').replaceWith(origDiv)
      }
    } else {
      jiorn.value.textContent = "Здесь пока ничего нет! Перейдите в раздел 'Ассортимент', чтобы сделать заказ!"
    }
  }}
console.log(tulup57)

  wow('append')

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

