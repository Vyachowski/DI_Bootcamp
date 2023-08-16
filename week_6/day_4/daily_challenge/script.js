// 🌟 Exercise 1 : List Of People
// Instructions
const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.
people.shift();

console.log(people); // -> ['Mary', 'Devon', 'James']
// Write code to replace “James” to “Jason”.
people.splice(2, 1, 'Jason');

console.log(people); // -> ['Mary', 'Devon', 'Jason']
// Write code to add your name to the end of the people array.
people.push('Slava');
console.log(people); // -> ['Mary', 'Devon', 'James', 'Jason', 'Slava]
// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
console.log(people.indexOf('Mary')) // -> 0
// Write code to make a copy of the people array using the slice method.

const newPeople = people.slice(1, 3);
console.log(newPeople); // -> ['Devon', 'Jason']
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
// Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(newPeople.indexOf('Foo')); // -> -1: because there is no such string in array
// Create a variable called last which value is the last element of the array.
const last = newPeople[newPeople.length - 1];
console.log(last); // -> Jason
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.
for (const person of people) {
  console.log(person);
}
// Using a loop, iterate through the people array and exit the loop after you console.log “Devon”
for (const person of people) {
  console.log(person);
  if (person === 'Devon') {
    break;
  }
}
// Hint: take a look at the break statement in the lesson.


// 🌟 Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus
const colors = ['cyan', 'magenta', 'yellow', 'black'];
const colorsLength = colors.length;

for (let i = 0; i < colorsLength; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// 🌟 Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// let answer = prompt('Give me a number, please.')
// console.log(typeof answer);
// // While the number is smaller than 10 continue asking the user for a new number.
// while (Number(answer) < 10) {
//   answer = prompt('Give me a number, please.')
// }
// Tip : Which while loop is more relevant for this situation?


// 🌟 Exercise 4 : Building Management
// Instructions:
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}


// Review About Objects
// Copy and paste the above object to your Javascript file.
// Console.log the number of floors in the building.
console.log(building.numberOfFloors);
// Console.log how many apartments are on the floors 1 and 3.
console.log(`Apartments on the first floor: ${building.numberOfAptByFloor.firstFloor}\nApartments on the third floor: ${building.numberOfAptByFloor.thirdFloor}`)
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log("Dan's info: ", building.nameOfTenants[1], building.numberOfRoomsAndRent.dan)
// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.


// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.
const family = {
  son: 'Slava',
  sibling: 'Gleb',
  mother: 'Lera',
  dad: 'Igor'
}

for (member in family) {
  console.log(member,' is ', family[member]);
}

// Exercise 6 : Rudolf
// Instructions
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
// Solution 1
for (detail in details) {
  console.log(detail, details[detail]);
}

// Solution 2
let string = '';
for (detail in details) {
  string = string + ' ' + detail + ' ' + details[detail];
}
console.log(string.trim());

// Exercise 7 : Secret Group
// Instructions
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”
const secretGroupName = names.toSorted().map((name) => name[0]);
console.log(secretGroupName); // -> “ABJKPS”