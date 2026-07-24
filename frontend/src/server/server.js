import express from 'express'
import https from 'https'
import fs from 'fs'
import cors from 'cors'
import {json} from 'express'
import multer from 'multer'
import cookieParser from 'cookie-parser';
import {MongoClient} from "mongodb";
import jwt from 'jsonwebtoken';
import {cookie} from "yarn/lib/cli.js";

let lila
let ord
const url = "mongodb://127.0.0.1:27017/"
const client = new MongoClient(url);
const db = client.db("order");
const collection = db.collection("orderdata")
const upload = multer({ dest: 'uploads/' });   // или memoryStorage
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use(cors({
    origin: 'https://localhost:5173', // MUST be the exact URL, NOT '*'
    credentials: true                 // Required when withCredentials is true
}));
app.use(cookieParser())

app.use(express.json());

const options = {
    key: fs.readFileSync('C:\\Windows\\System32\\localhost+2-key.pem'),
    cert: fs.readFileSync('C:\\Windows\\System32\\localhost+2.pem'),
};
/*function saviurMiddleware() {
    if (!topken) {
        window.topken = req.body
    } else {

    }
} */



async function run(informa) {
    try {
        await client.connect();
        console.log("Подключение установлено");
        informa.usr= lila
        ord = informa
        console.log(ord)
        console.log(informa)
        const result2 = await collection.findOne(informa)
        console.log(result2)
        if (result2) {
            let ggs = await db.collection('orderdata').deleteMany(informa);
            console.log(ggs)
        } else {
            const result = await collection.insertOne(informa);
            console.log(result)
        }
    }catch(err) {
        console.log(err);
    } finally {
        await client.close();
        console.log("Подключение закрыто")
    }
}

async function run3(informa) {
    try {
        await client.connect();
        console.log("Подключение установлено");
        console.log(informa);
        const collection = db.collection("logindata")
        const result2 = await collection.findOne(informa)
        console.log(result2)
        if (result2) {
            let ggs = await db.collection('logindata').deleteMany(informa);
            console.log(ggs)
        } else {
            const result = await collection.insertOne(informa);
            console.log(result)
        }
    }catch(err) {
        console.log(err);
    } finally {
        await client.close();
        console.log("Подключение закрыто")
    }
}

async function run2(informa) {
    try {
        await client.connect();
        console.log("Подключение установлено");
        const result2 = await collection.findOne(informa)
        console.log(result2)
        response.send(result2)
    }catch(err) {
        console.log(err);
    } finally {
        await client.close();
        console.log("Подключение закрыто")

    }
}
//import axios from 'axios'

function auMiddleware(req, res, next) {
    let celsw = req.body
    console.log(req.body)
    const lalalay = jwt.sign({ celsw }, 'НАЮЖАСОМБАДИЗАДАЮСТУНОУ');
    console.log(req.payload)
    console.log(`${celsw} - 51`)
    console.log(`${lalalay} - 52`)
    // const cook = `jwtk=${lalalay}; HttpOnly; Secure; SameSite`
    //res.setHeader('Set-Cookie', cook)
   // res.send(req.user) // ✅ return прервет выполнение, next() не нужен
    req.user = lalalay
    console.log(req.user)
  //  res.send(req.user)
    next()

}

app.post("/logpost", auMiddleware, function(requeste, response){
                console.log('8ogud')
                try {
                    const tralala = requeste.user
                    let objj = {usr: tralala, dt: requeste.body}
                    console.log('138')
                    console.log(objj)
                    run3(objj)
                    console.log('135')
                    const decoded = jwt.verify(requeste.user, 'НАЮЖАСОМБАДИЗАДАЮСТУНОУ');
                    console.log(decoded)
                    requeste.user = decoded; // ✅ Просто сохраняем данные в объект запроса
                    response.send(decoded.celsw.login)
                } catch (e) {
                    //res.status(403).send("Невалидный токен");
                    return response.status(403).send(e);}
});


app.get("/logpost", function(request, response){
   console.log(request.cookies.jwtk)
});

app.post("/orderee", function(request, response){
    if (lila) {
        let orderL = Object.entries(ord)
        let jj = []
        for (let o of orderL) {
            if (o[0] != 'usr' && o[0] != '_id') {
                jj.push(o)
            }
        }
        console.log(jj)
        response.send(jj)
    } else {
        response.send('регистрируйся вонючка')
    }

});

app.post("/blogpostee", function(request, response){
    let data = ''
    request.on("data", chunk => {
        data += chunk;
    });
    request.on("end", () => {
        data = JSON.parse(data)
        console.log(data)
        run2(data)
    });
});


app.post("/blogpost", function(request, response){
    console.log(request.body)
});

https.createServer(options, app).listen(3000, () => {
    console.log('Express HTTPS сервер запущен на https://localhost:3000');
});
console.log("Запущено")