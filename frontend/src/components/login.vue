<script setup>
import {onMounted, ref, watch} from "vue";
//import jwt from 'jsonwebtoken';
//import jwt from 'jsonwebtoken'
//import 'jsonwebtoken'



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
let logi = ref()
let passw = ref()
let adres = ref()
let syia = ref()

function texton() {
  let logO = {}
  logO.login = logi.value
  logO.password = passw.value
  logO.adresl = adres.value
  let bruh = JSON.stringify(logO)
  const req = new XMLHttpRequest()
  req.open("POST", "http://127.0.0.1:8000/postuser/")
  req.withCredentials = true;
  req.setRequestHeader('Content-Type', 'application/json');
  console.log(bruh)
  req.send(bruh)
  req.onload = () => {
    console.log(req.response)
    switch (req.response) {
      case 'LoginCommonWordError':
        syia.value.textContent='>Поле не должно содержать слово "login"'
        break
      case 'PasswordCommonWordError':
        syia.value.textContent='>Поле не должно содержать слово "password"'
        break
      case 'AdreslCommonWordError':
        syia.value.textContent='>Поле не должно содержать слово "adresl". Это системное имя.'
        break
      case 'LoginTooLongError':
        syia.value.textContent='Логин не может быть длинее 30 символов'
        break
      case 'PasswordTooLongError':
        syia.value.textContent='Пароль не может быть длинее 30 символов'
        break
      case 'PasswordTooShortError':
        syia.value.textContent='Пароль не может быть короче 10 символов'
        break
    }
  //  sessionStorage.setItem("username", req.response);
  }
}
</script>
<template>
  <div class="garden eerie" ref="abt">
  <form>
    <fieldset>
      <input type="text" class="inpl" id="login" placeholder="Логин" v-model="logi">
    </fieldset>
    <fieldset>
      <input type="text" class="inpl" id="password" placeholder="Пароль" v-model="passw">
    </fieldset>
    <fieldset>
      <input type="text" class="inpl" id="password" placeholder="Адрес" v-model="adres">
    </fieldset>
    <button type="submit" id="submitexpert" @click.stop.prevent="texton">Подтвердить</button>
    <p id="syia" ref="syia"></p>
  </form>
  </div>
</template>