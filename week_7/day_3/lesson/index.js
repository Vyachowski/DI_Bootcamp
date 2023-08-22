// LINK - Scoping
let b = 3; d = b; u = b;

const tree = ++d * d * b * b++ + // -> 4 * $ * 3 * 3 + 
+ --d + + +b-- + // -> 3 + 4 +
+ +d*b+ + // -> 3 * 3 +
u // -> 3

console.log(tree); // -> 163

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

