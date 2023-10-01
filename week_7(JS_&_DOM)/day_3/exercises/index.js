// 🌟 Exercise 1 : Scope
// Instructions
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.
// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// ANSWER -> It will be 3, just a regular flow of the code

// #1.1 - run in the console:
// funcOne()
// #1.2 What will happen if the variable is declared 
// with const instead of let ?

// ANSWER -> It will be an error (anyway a will not change), something like you cannot redeclare a constant variable

// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree() // ANSWER -> a = 0
// funcTwo()
// funcThree() // ANSWER -> a = 5

// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?

// Answer -> will fall with an error

// //#3
// function funcFour() {
//     window.a = "hello";
// }

// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // // #3.1 - run in the console:
// funcFour()
// funcFive()

// ANSWER -> As I understand window.a is not equal or not a reference of a variable «a» so nothing will be changed

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }

// ANSWER -> a will have a «test» value

// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// ANSWER -> In this case it is not important, they are in different scopes (function scope)

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);


// ANSWER -> in if scope it will be 5, outside if scope it will be 2, because global scope don't have an access to inner scope

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?

// ANSWER -> Nothing will change

// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:
// function winBattle(){
//     return true;
// };

// Transform the winBattle() function to an arrow function.
const winBattle = () => true;
// Create a variable called experiencePoints.
let experiencePoints;
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
winBattle() ? experiencePoints = 10 : experiencePoints = 1;
// Console.log the experiencePoints variable.
console.log(experiencePoints);

// 🌟 Exercise 3 : Is It A String ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output.
function isString(obj) {
  return (typeof obj === 'string');
}

// Example:
console.log(isString('hello')); // -> true
console.log(isString([1, 2, 4, 0])); // -> false


// 🌟 Exercise 4 : Find The Sum
// Instructions:
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
const sum = (a, b) => a + b;

// 🌟 Exercise 5 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

// First, use function declaration and invoke it.
// function convertKilogrammToGramm(kilogramms) {
//   const KILOGRAMM_IN_GRAMMS = 1000;
//   return kilogramms * KILOGRAMM_IN_GRAMMS;
// }

// console.log(convertKilogrammToGramm(3)) // -> 3000
// Then, use function expression and invoke it.
// const convertKilogrammToGramm = function(kilogramms) {
//   const KILOGRAMM_IN_GRAMMS = 1000;
//   return kilogramms * KILOGRAMM_IN_GRAMMS;
// }

// console.log(convertKilogrammToGramm(3)) // -> 3000
// Write in a one line comment, the difference between function declaration and function expression.
// Finally, use a one line arrow function and invoke it.
// const convertKilogrammToGramm = (kilogramms) => kilogramms * 1000;

// console.log(convertKilogrammToGramm(3)) // -> 3000
// 🌟 Exercise 6 : Fortune Teller
// Instructions:
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."
(function fortuneTeller(childrensNumber, partnersName, location, jobTitle) {
  const paragraph = document.createElement('p');
  paragraph.textContent = `You will be a ${jobTitle} in ${location}, and married to ${partnersName} with ${childrensNumber} kids.`;
  document.body.append(paragraph);
})(3,'bobr','Lousianna','CEO');

// 🌟 Exercise 7 : Welcome
// Instructions:
// John has just signed in to your website and you want to welcome him.
// Create a Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the navba (I added nav to header to make it more semantic), displaying the name of the user and his profile picture.
(function createWelcomeBanner(userName) {
  const navbar = document.createElement('nav');
  const image = document.createElement('img');
  image.setAttribute('src','avatar.jpeg');
  navbar.textContent = `Hello, ${userName}.`;
  document.querySelector('header').append(navbar);
  document.querySelector('header').append(image);
})('John');

// 🌟 Exercise 8 : Juice Bar
// Instructions:
// You will use nested functions, to open a new juice bar.
// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.
function displayOutput(text) {
  const drinksElement = document.getElementsByClassName('drinks');
  drinksElement.textContent += `${text}`;
}

// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like 
// "The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".
function makeJuice(size) {
  function addIngredients(firstIngredient, secondIngredient, thirdIngredient) {
    const sentence = `The client wants a ${size} juice, containing ${firstIngredient}, ${secondIngredient}, ${thirdIngredient}`;
    displayOutput(sentence);
  }

  addIngredients('beer', 'lime', 'pineapple');
}
// Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.
makeJuice('small');

// Part II:
// In the makeJuice function, create an empty array named ingredients.
// The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.
// Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".
// !! displayOutput was created before !!
function makeJuiceWithIngredients(size) {
  const ingredients = [];

  function addIngredientsToArr(firstIngredient, secondIngredient, thirdIngredient) {
    ingredients.push(firstIngredient, secondIngredient, thirdIngredient);
  }

  function displayJuice() {
    const sentence = `The client wants a ${size} juice, containing ${ingredients.join(', ')}`;
    displayOutput(sentence);
  }

  addIngredientsToArr('ice', 'mango', 'chili');
  addIngredientsToArr('beer', 'milk', 'potato :)');
  displayJuice();
}
// The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.
makeJuiceWithIngredients('medium');