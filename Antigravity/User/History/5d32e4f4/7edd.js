const api = 'https://dummyjson.com/test'

fetch(api).then(res => res.json()).then(data => console.log(data))