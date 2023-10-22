// Exercise 1 : Divisible By Three
// Instructions
let numbers = [123, 8409, 100053, 333333333, 7]
// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log true or false.
for (const number of numbers) {
  console.log((number % 3 === 0 ? true : false));
}

// Exercise 2 : Attendance
// Instructions
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

// Given the object above where the key is the student’s name and the value is the country they are from.
// Prompt the student for their name.
const answer = prompt('What is your name stranger?').toLowerCase();
if (answer in guestList) {
  console.log(`Hi! I'm ${answer}, and I'm from ${guestList[answer]}.`)
} else {
  // If the name is in the object, console.log the name of the student and the country they come from.
  // For example: "Hi! I'm [name], and I'm from [country]."
  // Hint: You don’t need to use a for loop, just look up the statement if ... in
  // If the name is not in the object, console.log: "Hi! I'm a guest."
  console.log("Hi! I'm a guest.")
}

// Exercise 3 : Playing With Numbers
// Instructions
let age = [20, 5, 12, 43, 98, 55];
// Requirements : Don’t use built-in Javascript methods to answer the following questions. You have to create the logic by yourself. Use simple for loops.

// 1. Console.log the sum of all the numbers in the age array.
let result = 0;
for (const number of age) {
  result += number;
}
console.log(result);

// 2. Console.log the highest age in the array.
result = 0;

for (const number of age) {
  number > result ? result = number : result;
}

console.log(result);