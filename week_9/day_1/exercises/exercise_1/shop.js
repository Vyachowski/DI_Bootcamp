// – Create another file named shop.js.
// – In shop.js, require the product objects from the products.js module.
// – Create a function that takes a product name as a parameter and searches for the corresponding product object.
// – Call this function with different product names and print the details of the products.
// – Run shop.js and verify that the correct product details are displayed.

const products = require('./products');

function findProduct(productName) {
  const productNames = products.map((product) => product.name);
  const indexOfRequestedProduct = productNames.indexOf(productName);
  return products[indexOfRequestedProduct];
}

console.log(findProduct('bottle')); //  -> { name: 'bottle', price: 12, category: 'miscellaneous' }
console.log(findProduct('jar')); //  -> { name: 'bottle', price: 12, category: 'miscellaneous' }
console.log(findProduct('coke')); //  -> { name: 'bottle', price: 12, category: 'miscellaneous' }