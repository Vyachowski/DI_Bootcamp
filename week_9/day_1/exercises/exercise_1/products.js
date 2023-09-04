// 🌟 Exercise 1: Multiple Exports And Import Using CommonJS Syntax
// Instructions
// – Create a file named products.js.
// – Inside products.js, create an array of objects, each representing a product with properties like name, price, and category.
// – Export this array using the Common JS syntax.


const products = [
  {
    name: 'bottle',
    price: 12,
    category: 'miscellaneous'
  },
  {
    name: 'jar',
    price: 15,
    category: 'miscellaneous'
  },
  {
    name: 'coke',
    price: 2,
    category: 'drinks'
  },
]

module.exports = products;