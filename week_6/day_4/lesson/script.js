// Console.log
// console.log('Hello world!');
// console.log('Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, quisquam cumque dolorem alias ea rerum soluta consequuntur, dolor hic, dolore ratione praesentium nam necessitatibus tempore expedita totam natus facilis iste?');

// // Variables
// let x = 3;
// let X = 4;
// console.log(x);
// console.log(X);
// let myName = 'Pizhon';
// console.log(myName);

// // Camel case
// let myName = 'Slava';

// // Undefined

// let a;
// console.log(a);


// // Data Types
// let exampleString = 'Hello';
// let exampleString2 = 'World';
// console.log(exampleString + ' ' + exampleString2);
// console.log('2');

// let longString = 'This si a very long string \
// which need to be so long that\
// it srLorem ipsum dolor sit amet consectetur adipisicing elit. Et, quisquam cumque dolorem alias ea rerum soluta consequuntur, dolor hic, \
// dolore ratione praesentium nam necessitatibus tempore expedita totam natus facilis iste?'

// console.log(longString);

// String properties and methods
// let myName = 'Slava';
// console.log(myName.length);

// // IndexOf
// console.log(myName.indexOf('S'));
// console.log(myName.indexOf('B'));

// // Substring
// console.log(myName.substring(1, 4));

// // toLowerCase & toUpperCase
// let myString = "DON'T YELL on me!!!!!!";
// console.log(myString.toLowerCase());
// console.log(myString.toUpperCase());


// // Exercise 1
// const addressNumber = '10';
// const addressStreet = 'Jungle Street';
// const country = 'Croatia';

// const globalAddress = `I live in ${addressStreet} ${addressNumber}, ${country}`;

// console.log(globalAddress);

// // Number methods
// let op = 'me';
// console.log(isNaN(op));

// // toString
// let ten = 10;
// console.log(ten);
// console.log(ten.toString());

// // Comparison
// console.log(1 === 1);
// let x = 2;
// console.log(x == '2');
// console.log(x === '2');
// console.log(x === 2);
// // not equal
// console.log(x != 2); // false
// console.log(x !== 2); // false
// console.log(x != '2'); // false
// console.log(x !== '2'); // true
// console.log(x >= 2); // true
// console.log(x > 1 && x < 3) // true

// User interface functions
// Alert
// alert('Welcome to my website!');
// console.log('After alerts!')
// // Prompt
// const userAnswer = prompt('What is your name?', 'Bobrishka');
// console.log(`Hello, welcome to my website ${userAnswer}`);
// // Confirm
// let isBoss = confirm('Are you the boss?');
// console.log(isBoss);
// alert(isBoss);

// // Arrays
// let users = ['Daniel', 'Bobr', 'Ondatr'];
// let x = '1';
// console.log(typeof users);

// let colors = ['blue', 'yellow', 'green', 54];
// console.log(colors[3]);

// let arrayCeption = [
//   [1,2,3],
//   [5,6,7,8],
//   [1, 13, 15]
// ];

// console.log(arrayCeption[0][1]);

// let colors = ['Pink', 'Blue', 'Green'];
// console.log(colors);
// colors[1] = 'Yellow';
// console.log(colors);
// colors.push('Yellow');
// console.log(colors);

// // remove element of array
// colors.pop();
// console.log(colors);


// Splice array

let colors = ['Blue', 'Yellow', 'Green'];
console.log(colors);

colors.splice(1, 2, 'Pink', 'Orange', 'Grey');

console.log(colors);