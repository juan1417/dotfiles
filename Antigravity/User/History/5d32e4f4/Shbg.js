const api = 'https://dummyjson.com/test'

fetch('https://dummyjson.com/products')
.then(res => res.json())
.then(console.log);