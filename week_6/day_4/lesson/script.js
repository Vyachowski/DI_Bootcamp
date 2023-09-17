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

// let colors = ['Blue', 'Yellow', 'Green'];
// console.log(colors);

// colors.splice(1, 2, 'Pink', 'Orange', 'Grey');

// console.log(colors);

// Slice

// let colors = ['Blue', 'Yellow', 'Green', 'Red'];

// let slicedArray = colors.slice(1, 3);

// console.log(colors);
// console.log(slicedArray);

// const pets = ['dog', 'cat', 'fish', 'rabbit', 'cow'];

// console.log(pets[0]);

// pets.push('horse');
// console.log(pets);
// pets.splice(3, 1);
// console.log(pets);

// let person = {
//   firstName: 'Slava',
//   lastName: 'Haikin',
//   age: 34,
//   eyeColor: 'blue'
// }

// console.log(person.firstName);
// console.log(person['firstName']);

// // Add or change variables

// person.country = 'Israel';
// console.log(person);

// // Delete from object
// delete person.age;
// console.log(person);


// let x = 16;
// // x = 18;
// // x = 21;

// if (x >= 21) {
//   console.log('You can drink in the US');
// }

// else if (x >= 18) {
//   console.log('You can drink in Russia');
// }

// else {
//   console.log('You are to young to drink');
// }


// Exercise Keyless react-exercise

// const userAnswer = Number(prompt('What is your age'));

// if (userAnswer < 18) {
//   alert('Sorry, you are to young to drive this react-exercise')
// } else if (userAnswer === 18) {
//   alert('Congratulions of your first year of driving')
// } else {
//   alert('Powering On. Enjoy the ride!')
// }


// let fruit = 'Papayas';
// // fruit = 'Apples';

// switch (fruit) {
//   case 'Oranges':
//     console.log('It is orange! It cost: 6 bucks per kilo');
//     break;
//     case 'Mangoes':
//       console.log('It is mango! It cost: 6 bucks per kilo');
//       break;
//     case 'Bulbatini':
//     case 'Papayas':
//       console.log('It is papaya! It cost: 122 bucks per kilo');
//       break;
//     default:
//       console.log('Sorry, we are out of ' + fruit);
// }

// Loops
// // For loop

// for (let i = 0; i < 5; i++) {
//   console.log('the current number is ' + i)
// }

// let colors = ['red', 'blue', 'pink', 'red'];

// for (let i = 0; i < colors.length; i++) {
//   console.log('the ' + (i + 1) + ' color is ' + colors[i]);
// }

// // Loops FOR/IN OBJECT

// let person = {
//   name: 'Daniel',
//   age: '26',
//   country: 'Israel'
// }

// for (let x in person) {
//   console.log(x);
//   console.log(person[x]);
// }

// console.log(person.name)

// // Loops FOR/OF

// let colors = ['red', 'blue', 'pink', 'red'];

// for (let color of colors) {
//   console.log(color);
// }

// // While Loop

// let n = 0;

// while (n < 3) {
//   console.log(n);
//   n++;
// }

// let answer = prompt('What is the secret password?');

// while (answer != '1234') {
//   answer = prompt('What is the secret password?');
// }

// alert('Welcome Admin');


// // While-Do Loop
// let i = 0;
// do {
//   console.log('The number is' + 1);
//   i++;
// }
// while (i < 10);

// // Break statement

// for (let i = 0; i < 5; i++) {
//   if (i === 3) {
//     break
//   }
//   console.log(i);
// }

// for (let i = 0; i < 10; i++) {
//   if (i === 3) {
//     console.log('And here is a moment when we are skipping number 3')
//     continue;
//   }
//   console.log(i);
// }

let myPeople = 'go';

const yourName = 'Vladlena';

console.log(yourName);