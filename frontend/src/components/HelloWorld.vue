<template>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <div class="font-normal text-xl center garden" ref="glava">
  <div class="items-center justify-center mb-60 blackT">
    <header>
      <img src="https://cdn-icons-png.flaticon.com/512/5515/5515950.png" class=" size-16 relative top-15 left-60" @click="alarm">
      <h1 class="w-1/2 text-7xl m-auto center">Магазин Цветочков</h1>
      <form>
        <label for="referrer">Выберите тему:
          <select id="referrer" name="referrer" v-model="selected">
            <option value=""  >(Выберете тему)</option>
            <option value="1" @click="blackTheme">Ботанический сад</option>
            <option value="2" @click="orangeTheme">Пустынный оазис</option>
            <option value="3" @click="blueTheme">Подводный вулкан</option>
            <option value="4" @click="pinkTheme">Пленительная помада</option>
            <option value="5" @click="limeTheme">Ядовитый плющ</option>
          </select>
        </label>
      </form>
      <p>У нас есть довольно широкий ассортимент различных цветов, который будет представлен ниже. Чтобы сделать заказ свяжитесь с нашим <a href="https://t.me/flower_shop_bot_bot">ботом</a>.</p>
    </header>
    <div class="flex mt-10 -row-end-1" >
      <figure class="">
        <img src="https://oneironauticum.com/wp-content/uploads/2015/04/red-spider-lily-200x200.jpg">
        <figcaption class="photo ">Павучья лилия</figcaption>
      </figure>
      <figure>
        <img src="https://sun9-56.userapi.com/s/v1/ig2/Kc6w6ZV6mXoxdkoIyeEcinbteQJJPBGTunn_2cwSF8yMBd56nr79zpdWwM0Hd3gw6qZdHWiezlgjm8GpGMV5xG_W.jpg?size=200x200&quality=96&crop=100,0,599,599&ava=1">
        <figcaption class="photo">Роза</figcaption>
      </figure>
      <figure>
        <img src="https://sun1-83.userapi.com/s/v1/ig2/m8Y1VEWadTCKYkoZ6Y8QTfW-jody6G2r23-SfxCce1Mp8TcZrD0FgltWZku6JJ7OQPx5Bj_CtZI5TdKUCrN8CEwi.jpg?size=200x200&quality=95&crop=0,163,639,639&ava=1">
        <figcaption class="photo">Много роз</figcaption>
      </figure>
      <figure>
        <img src="https://sun9-41.userapi.com/s/v1/if1/zN-7WzEIuJ6tCxblSGko3P0s_Zqu2fXHyvb1m1UY5sjDNC09hXjmH7RSFRrvz8TbHnjS4O7k.jpg?size=200x200&quality=96&crop=215,4,890,890&ava=1">
        <figcaption class="photo">Ещё больше роз</figcaption>
      </figure>
      <figure>
        <img src="https://sun9-4.userapi.com/s/v1/ig2/DoLRzoweSAvnREf--Ll7GYt5zOfZN6KUqD_h6gKHzHJ-pT5rQPyccXMVka5mTaF-rVW36SZSI01tAIGlh5-0lky7.jpg?size=200x200&quality=96&crop=80,80,479,479&ava=1">
        <figcaption class="photo">Красные розы</figcaption>
      </figure>
      <figure>
        <img src="https://sun9-49.userapi.com/s/v1/ig2/GK1k_Jkjm7AuTWhM4lCFkilKvcJWyfkljDaIcZbC06ED9QPiAIkCcWsmYaOtcrnv8PQ8Ju38F6K7qo_HV8n65qHW.jpg?size=200x200&quality=95&crop=3,3,1197,1197&ava=1">
        <figcaption class="photo">Маленькие фиолетовые цветочки</figcaption>
      </figure>
      <figure>
        <img src="https://pp.userapi.com/c840735/v840735514/13fd5/XIZ0ektPGKg.jpg">
        <figcaption class="photo">Букет цветочков</figcaption>
      </figure>
      <figure>
        <img src="https://sun9-36.userapi.com/s/v1/if1/Og-7mEmewonBw63ETXHGUjNQb621WDzzmWWDcgseloW6PPn_B7HolpFfCpIjBF6LPxCSsVRM.jpg?size=200x200&quality=96&crop=8,11,200,200&ava=1">
        <figcaption class="photo">Нарисованные ромашки</figcaption>
      </figure>
      <figure>
        <img src="https://sun9-69.userapi.com/s/v1/if1/ftcTrYzLph4Woshjr5sBU9lCKFUY-IltXHLXNyZAvUL3c01hnNN7TMivUvOnV6lEFZqKE1eO.jpg?size=200x200&quality=96&crop=0,207,1012,1012&ava=1">
        <figcaption class="photo">Лотосы</figcaption>
      </figure>
    </div>
    <div class="hr"></div>
    <h2 class="card text-2xl font-bold center">Наш ассортимент:</h2>
    <div class="flex m-auto items-center justify-center">
      <ul class="list-disc">
        <li>Азалия Индика Красная</li>
        <li>Венерина Мухоловка 'Змей Горыныч'</li>
        <li>Антуриум Андреанум красный</li>
        <div class="flower">
          <div id="1" class="leaf"></div>
          <div id="2" class="leaf"></div>
          <div id="3" class="leaf"></div>
          <div id="4" class="leaf"></div>
          <div id="5" class="leaf"></div>
        </div>
        <li>Орхидея Фаленопсис</li>
        <li>Фикус бенджамин мокламе</li>
        <li>Черноголовка</li>
        <li>Хризантема мультифлора</li>
        <li>Аргирантемум</li>
        <li>Лейя изящная</li>
        <li>Астра альпийская</li>
        <li>Исскуственные</li>
        <li>И другие (см фото)</li>
      </ul>
    </div>
    <div>
      <figure>
        <a href="https://rutube.ru/video/c6cc4d620b1d4338901770a44b3e82f4/?r=wd"><img src="https://avatars.mds.yandex.net/get-yapic/48449/Fnupek273L0AWNvyiPeHwK9Es4-1/orig" class="m-auto"></a>
        <figcaption class="center">Кликни сюда, чтобы увидеть видео про нас</figcaption>
      </figure>
    </div>
    <div class="hr"></div>
    <h2 class="text-2xl font-bold center">Хотите сотрудничать?</h2>
    <h3 class="text-xl font-bold center ">Свяжитесь с нами!</h3>
    <div class="center" :class="{ blackT: isBlack, orangeT: isOrange, blueT: isBlue, pinkT: isPink, limeT: isLime, }">
      <form>
        <fieldset>
          <legend>Введите вашу электронную почту:</legend>
          <label for="email"><input id="email" type="email" v-model="datadis1" autocomplete="off"  required></label>
        </fieldset>
        <fieldset>
          <legend>Введите ваш номер телефона:</legend>
          <label for="number"><input id="number" type="tel" v-model="datadis2" required></label>
        </fieldset>
        <fieldset>
          <legend>Для чего вы связываетесь с нами?</legend>
          <label  for="radd"><input id="radd" name="radio-field" type="radio" value="sotud" @click="dis3sotr" checked>Хочу сотрудничать</label>
          <label for="raddd"><input id="raddd" type="radio" name="radio-field" value="opt" @click="dis3opt" >Хочу сделать заказ оптом</label>
        </fieldset>
        <input type="submit" value="Отправить!" @click.prevent="displayD"/>
      </form>
    </div>
    <p v-if="dDisplay" class="center" :class="{ blackT: isBlack, orangeT: isOrange, blueT: isBlue, pinkT: isPink, limeT: isLime, }">Ваши данные:
      Почта: {{datadis1}}; Номер: {{datadis2}}; {{datadis3}}</p>
  </div>
  </div>
</template>
<script setup>
import { ref, watch } from 'vue'
let isBlack = ref(true)
let isOrange = ref(false)
let isBlue = ref(false)
let isPink = ref(false)
let isLime = ref(false)
let dDisplay = ref(false)
const datadis1 = ref('')
const datadis2 = ref('')
const datadis3 = ref("Желаете сотрудничать ?")
console.log(glava)


function blackTheme() {
  glava.value.className =  'font-normal text-xl center garden'
}
function orangeTheme() {
  glava.value.className =  'font-normal text-xl center oasis'
}
function blueTheme() {
  glava.value.className =  'font-normal text-xl center volcano'
}
function pinkTheme() {
  glava.value.className =  'font-normal text-xl center lipstic'
}
function limeTheme() {
  glava.value.className =  'font-normal text-xl center poison'
}
function alarm() {
  alert("Наш цветочный магазин имеет очень большую историю. Мы ведём нашу деятельность с 1999 года. С тех пор наша сеть развилась до междугороднего уровня, а сами мы стали профессионалами с большимс опытом в своём деле. блаблаблаблабла")
}
function displayD() {
  dDisplay.value = true;
}
function dis3sotr() {
  datadis3.value = "Желаете сотрудничать."
}
function dis3opt() {
  datadis3.value = "Желаете купить товар оптом."
}

const selected = ref('');

watch(selected, (newVal, oldVal) => {
  if (newVal === "1") {
    blackTheme();
  } else if (newVal === "2") {
    orangeTheme();
  } else if (newVal === "3") {
    blueTheme();
  } else if (newVal === "4") {
    pinkTheme();
  } else if (newVal === "5") {
    limeTheme();
  }
});

</script>
