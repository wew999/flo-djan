import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import fs from 'fs' // 👈 Подключаем модуль для чтения файлов


// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss()],
    server: {
        port: 5173,
        https: {
            key: fs.readFileSync('C:\\Windows\\System32\\localhost+2-key.pem'),
            cert: fs.readFileSync('C:\\Windows\\System32\\localhost+2.pem')
        }
    }
})
