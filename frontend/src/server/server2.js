import express from 'express'
import http from 'http'
import fs from 'fs'
import cors from 'cors'
import {json} from 'express'
import multer from 'multer'
const upload = multer({ dest: 'uploads/' });   // или memoryStorage
const app = express();
import {MongoClient} from "mongodb";
const url = "mongodb://127.0.0.1:27017/"
const client = new MongoClient(url);
const db = client.db("order");
const collection = db.collection("orderdata")
import jwt from 'jsonwebtoken';
import {cookie} from "yarn/lib/cli.js";
let lila
let ord
import cookieParser from 'cookie-parser';
app.use(cors());
app.use(cookieParser())


app.post("/cookietra", function(request, response){
    let data = ''
    request.on("data", chunk => {
        data += chunk;
    });
    request.on("end", () => {
        const myCookie = request.cookies['jwtk'];
        console.log(`${myCookie} - КУКИ ЗАПРОСААААААА`)
        /*data = JSON.parse(data)
        const lalalay = jwt.sign({ data }, 'НАЮЖАСОМБАДИЗАДАЮСТУНОУ');
        console.log(data)
        console.log(lalalay)
        run3({udata: lalalay})
        const cook = `jwtk=${lalalay}; HttpOnly; Secure`
        lila = lalalay
        response.setHeader('Set-Cookie', cook)
        response.send("y") */
    });
});

app.listen(6767);
console.log("Запущено")