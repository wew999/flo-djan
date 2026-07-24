import { ref} from 'vue'
export function themeMemory() {
    window.cookieStore.addEventListener('change', () => {
        let balsalmt = document.cookie
        const farts = balsalmt.split("=")
        console.log(farts)
        if (farts[1]) {
            scorn.value = farts[1]
            console.log(scorn.value)
        }
    });
    window.scorn = ref(document.cookie)
    console.log(scorn)
    const hhhsw = scorn.value.split("=")
    document.cookie=`theme=chirp`
    document.cookie=`theme=${hhhsw}`
    console.log(hhhsw)
    document.cookie = scorn.value
}