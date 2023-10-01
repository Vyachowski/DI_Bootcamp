const express = require('express');
require('dotenv').config()
const app = express();

app.listen(process.env.PORT, () => {
  console.log(`Run on port ${process.env.PORT}`);
})

const products = [
  { id: 1, name: 'iPhone', price: 800 },
  { id: 2, name: 'iPad', price: 700 },
  { id: 3, name: 'appleWatch', price: 600 },
]

app.get('/api/products/', (req, res) => {
  res.send(products);
});

app.get('/api/products/search', (req, res) => {
  console.log(products)
});

app.get('/api/products/:id', (req, res) => {
  const id = req.params.id;
  const product = products.find((item) => item.id === +id);
  res.json(product);
});

