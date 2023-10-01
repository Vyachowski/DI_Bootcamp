// // LINK - Scoping
// let b = 3; d = b; u = b;

// const tree = ++d * d * b * b++ + // -> 4 * $ * 3 * 3 + 
// + --d + + +b-- + // -> 3 + 4 +
// + +d*b+ + // -> 3 * 3 +
// u // -> 3

// console.log(tree); // -> 163

// LINK - Scoping
// let x = 8;
// {
//   x = 9;
// }

// console.log(x);

//LINK - Second example of defining functions
// for (let i = 1; i < 5; i++) {
//   console.log(i);
// }
// console.log(i); // -> Will give an error: i is not defined

// function x() {
//   let x = 8;
//   function y(){
//     let a = 7;
//     console.log(x);
//   }
//   // console.log(a); -> Will give an error
// }

// x();

// Default parameters
// function getXY(x, y) {
//   return x + y;
// }

// let sum = getXY(2, 3);
// console.log(sum);

// let y;
// let x = 5;
// if(x < 5) {
//   y = 10;
// } else {
//   y = 0;
// }

// let y = (x < 5) ? 6 : (x === 5) ? 'hi' : 'bye';



// Function properties
// function x () {
//   let hi = 'hello';
//   function y () {
//     console.log(hi);
//   }
//   return y;
// };

// let sayHi = x()();
// console.log(sayHi);

// function x(param) {
//   function y(param1) {
//     return param * param1;
//   }
//   return y;
// }

// const xArrow = (x) => {
//   return (y) => {
//     return x * y;
//   };
// };

// // Regular function
// const VAT = 1.17;
// let sum = x(VAT);
// console.log(sum);
// console.log('sum =>', sum(100));
// console.log('sum =>', sum(200));
// console.log('sum =>', sum(300));

// // Arrow function
// let sumWithArrow = xArrow(VAT);
// console.log(sumWithArrow);
// console.log('sum =>', sumWithArrow(100));
// console.log('sum =>', sumWithArrow(200));
// console.log('sum =>', sumWithArrow(300));


/* Compose */
const x = (a,b) => (c) => a(b(c));

const sum2 = (num) => num * 2;
const sum = (num) => num + 1;

let ret = x(sum2, sum)(6);
console.log('ret => ', ret);

let a = 'city';
let b = 'name';

let obj = {
  // name: 'John',
  [b]: 'John',
  age: 25,
  lastName: 'Doe',
  getFullName: function() {
    return this.name + '' + this.lastName;
  },
  [a]: 'Ramat Gan'
};

console.log(obj);
console.log(obj.name);
console.log(obj['name']);
console.log(obj[a]);