// Create another file named app.js.
// In app.js, import the array of person objects from the data.js module.
import data from './data.js';
// Write a function that calculates and prints the average age of all the persons in the array.
function calculateAverageAge(people) {
  const allPersonsAges = people.map((el) => el.age);
  const ageSum = allPersonsAges.reduce((acc, element) => {
    return acc + element;
  }, 0)
  return ageSum;
}
// Use the imported array and the average age function in app.js.
console.log(calculateAverageAge(data)); // -> 69
// Run app.js and confirm that the average age is correctly calculated and displayed