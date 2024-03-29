// Daily Challenge : Go Wildcats
const gameInfo = [
 {
   username: "john",
   team: "red",
   score: 5,
   items: ["ball", "book", "pen"]
 },
 {
   username: "becky",
   team: "blue",
   score: 10,
   items: ["tape", "backpack", "pen"]
 },
 {
   username: "susy",
   team: "red",
   score: 55,
   items: ["ball", "eraser", "pen"]
 },
 {
   username: "tyson",
   team: "green",
   score: 1,
   items: ["book", "pen"]
 },
];
// Create an array using forEach that contains all the usernames from the gameInfo array, add an exclamation point (ie. “!”) to the end of every username.
const userNames = [];
gameInfo.forEach((user) => userNames.push(user.username + '!'));
// console.log(userNames); // -> ['john!', 'becky!', 'susy!', 'tyson!']

// 2. Create an array using forEach that contains the usernames of all players with a score bigger than 5.
const highScoreGamers = [];
gameInfo.forEach((user) => user.score > 5 && highScoreGamers.push(user.username));
// console.log(highScoreGamers)// -> ['becky', 'susy']

// 3. Find and display the total score of the users. (Hint: The total score is 71)
const totalScore = gameInfo.reduce((acc, user) => acc + user.score, 0);
// console.log(totalScore)// -> 71


// Daily Challenge: Car Inventory

// Part I
// Use the cars inventory below:
const inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

// Create a function getCarHonda(carInventory) that takes a single parameter. carInventory‘s value is an array which is an inventory of cars (see the array of objects below)
// The function should:
// – loop through the array of object and return the first react-exercise with the name “Honda”.
// – then, return a string in the format This is a {car_make} {car_model} from {car_year}.
// Hint : Find an array method that returns the value of the first element in an array that pass a test.
function getCarHonda(carInventory) {
  const honda = carInventory.find(car => car.car_make.toLowerCase() === 'honda');
  return ((honda) && `This is a ${honda.car_make} ${honda.car_model} from ${honda.car_year}`);
}

// console.log(getCarHonda(inventory)); // -> This is a Honda Accord from 1983

// Part II
// Create a function sortCarInventoryByYear(carInventory) that takes a single parameter carInventory‘s value is an array which is an inventory of cars
// the function should return an inventory that is sorted by car_year, ascending.
// Hint : Check out this tutorial on the sort method
function sortCarInventoryByYear(carInventory) {
  return carInventory.sort((a, b) => a.car_year - b.car_year);
}

// console.log(sortCarInventoryByYear(inventory)); // VVVV
// [
//   { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
//   { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
//   { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
//   { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
//   { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
// ];