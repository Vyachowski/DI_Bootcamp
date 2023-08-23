// Exercise 1 : Analyzing The Map Method
// Instructions
// Analyze this code, what will be the output ?
// [1, 2, 3].map(num => {
//   if (typeof num === 'number') return num * 2;
//   return ;
// });

// ANSWERL [2, 4, 6]

// Exercise 2: Analyzing The Reduce Method
// Instructions
// Analyze this code, what will be the output ?
// [[0, 1], [2, 3]].reduce(
//   (acc, cur) => {
//     return acc.concat(cur);
//   },
//   [1, 2],
// );

// ANSWER: [1, 2, 0, 1, 2, 3]

// Exercise 3 : Analyze This Code
// Instructions
// Using this code:
// const arrayNum = [1, 2, 4, 5, 8, 9];
// const newArray = arrayNum.map((num, i) => {
//     console.log(num, i);
//     alert(num);
//     return num * 2;
// })
// What is the value of i ?

// ANSWER: ??? On each step it will be a new value

// Exercise 4 : Nested Arrays
// Instructions
// Using a method, take this array const array = [[1],[2],[3],[[[4]]],[[[5]]]] and modify it
// Bonus Try to do it on one line.
const array = [[1],[2],[3],[[[4]]],[[[5]]]];
// console.log(array.flat(2)); // -> [1,2,3,[4],[5]]

// Using a method, take this array 
const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];

// and modify it to look like this array: ["Hello young grasshopper!","you are","learning fast!"].
const flattenedArray = greeting.flat();

// Turn the greeting array into a string
// console.log(flattenedArray.join(' ')); // -> Hello young grasshopper! you are learning fast!

// Turn the trapped number 3 
const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
// into: [3]
// console.log(trapped.flat(Infinity)); // -> [3]


// Exercise 1: Sum Elements
// Instructions
// Write a JavaScript program to find the sum of all elements in an array.
const arrayOfNumbers = [1, 3, 5, 2, 3];

function sum(array) {
  return (array) && array.reduce((acc, number) => acc + number, 0)
}

console.log(sum(arrayOfNumbers)); // -> 14

// Exercise 2 : Remove Duplicates
// Instructions
// Write a JavaScript program to remove duplicate items in an array.
// Simpliest solution
const deleteDuplicatesFromArraySimple = (array) => {
  return [...new Set(array)];
}

// Working solution
const deleteDuplicatesFromArrayWithMap = (array) => {
  const result = [];
  array.map((el) => result.includes(el) ? el : result.push(el));
  return result;
}

// Working solution
const deleteDuplicatesFromArrayWithLoop = (array) => {
  const result = [];
  for (element of array) {
    result.includes(element) ? undefined : result.push(element);
  }
  return result;
}

// Good solution
const deleteDuplicatesFromArrayWithForEach = (array) => {
  const result = [];
  array.forEach((el) => { if (!result.includes(el)) { result.push(el) } });
  return result;
}

//Best solution
const deleteDuplicatesFromArrayWithShortCircuit = (array) => {
  const result = [];
  return array.forEach((el) => result.includes(el) || result.push(el))
}

const testArray = [1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 6, 6, 6]

// console.log(deleteDuplicatesFromArraySimple(testArray)); // -> [ 1, 2, 3, 4, 6 ]
// console.log(deleteDuplicatesFromArrayWithMap(testArray)); // -> [ 1, 2, 3, 4, 6 ]
// console.log(deleteDuplicatesFromArrayWithLoop(testArray)); // -> [ 1, 2, 3, 4, 6 ]
// console.log(deleteDuplicatesFromArrayWithForEach(testArray)); // -> [ 1, 2, 3, 4, 6 ]
// console.log(deleteDuplicatesFromArrayWithShortCircuit(testArray)); // -> [ 1, 2, 3, 4, 6 ]

// Exercise 3 : Remove Certain Values
// Instructions
// Write a JavaScript function to remove: null, 0, "", false, undefined and NaN values from an array.
const sampleArray = [NaN, 0, 15, false, -22, '',undefined, 47, null];

const removeNaN = (array) => array.filter((element) => typeof element === 'number' && (!isNaN(element) && element !== 0));
// console.log(removeNaN(sampleArray)); //-> [15, -22, 47]

// Exercise 4 : Repeat Please !
// Instructions
// Write a JavaScript function to concatenate a given string n times (default is 1).
// Create the repeat function yourself:
// console.log(repeat('Ha!',3));
// "Ha!Ha!Ha!"


// Exercise 5 : Turtle & Rabbit
// For this exercise, look at the lesson More JS methods.
// Using this code :
const startLine = '     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';

turtle = turtle.padStart(9);
rabbit = rabbit.padStart(9);
// Line up the Turtle and the Rabbit at the start line.
//     It should look like this:

//     '     ||<- Start line'
//     '       🐢'
//     '       🐇'

// What happens when you run :
turtle = turtle.trim().padEnd(9, '=');

// ANSWER: It will delete all spaces in line with a turtle and then add 9 equal signs after the turtle icon. Other words – turtle will win like in a story :)

console.log(startLine);
console.log(turtle);
console.log(rabbit);
