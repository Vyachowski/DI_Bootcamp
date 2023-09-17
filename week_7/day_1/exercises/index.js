// 🌟 Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
function displayNumbersDivisible() {
  let sum = 0;
  for (let i = 0; i <= 500; i++) {
    if (i % 23 === 0) {
      console.log(i);
      sum += i;
    }
  }

  console.log(sum);
}

// OUTCOME
displayNumbersDivisible();
// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
// 368 391 414 437 460 483
// Sum : 5313

// Bonus: Add a parameter divisor to the function.

// displayNumbersDivisible(divisor)
function displayGivenNumbersDivisible(number) {
  let sum = 0;
  for (let i = 0; i <= 500; i++) {
    if (i % number === 0) {
      console.log(i);
      sum += i;
    }
  }

  console.log(sum);
}

// OUTCOME
displayGivenNumbersDivisible(3);
displayGivenNumbersDivisible(45);
// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3 and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45 and their sum


// 🌟 Exercise 2 : Shopping List
// Instructions:
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
const shoppingList = ['banana', 'orange', 'apple'];
// Create a function called myBill() that takes no parameters.
function myBill() {
  let totalPrice = 0

  for (const item of shoppingList) {
    if (stock[item] > 0) {
      totalPrice = totalPrice + prices[item];
      stock[item] = stock[item] - 1;
    } 
  }
  return totalPrice;
}
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.

// OUTCOME
console.log(myBill()) // -> 5.5
console.log(stock['banana']); // -> 5
// Bonus: If the item is in stock, decrease the item’s stock by 1


// Exercise 3 : What’s In My Wallet ?
// Instructions
// Note: Read the illustration (point 4), while reading the instructions
// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments: 
// – an item price
// – and an array representing the amount of change in your pocket.
// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01

function changeEnough(itemPrice, amountOfChange) {
  [quarters, dimes, nickel, penny] = amountOfChange;
  let totalSum = 0;

  const QUARTERNOMINAL = 0.25;
  const DIMESNOMINAL = 0.1;
  const NICKELNOMINAL = 0.05;
  const PENNYNOMINAL = 0.01;

  totalSum = (quarters * QUARTERNOMINAL) + (dimes * DIMESNOMINAL) + (nickel * NICKELNOMINAL) + (penny * PENNYNOMINAL);

  return totalSum >= itemPrice;
}

// 4. To illustrate:

// After you created the function, invoke it like this:

// changeEnough(4.25, [25, 20, 5, 0])
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)


// OUTCOME

console.log(changeEnough(14.11, [2,100,0,0])) // => returns false
console.log(changeEnough(0.75, [0,0,20,5])) // => returns true


// 🌟 Exercise 4 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:
// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
function hotelCost() {
  let totalPrice = 0;
  let answer = '';
  let nightsInHotel = 0;
  const pricePerNight = 140;

  while (nightsInHotel === 0 ) {
    answer = prompt('How long do you want to stay?');
    isNaN(Number(answer)) ? 0 : nightsInHotel = Number(answer);
  }
  totalPrice = nightsInHotel * pricePerNight;
  return totalPrice;
}

// console.log(hotelCost()); // -> for 10 days = 1400

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

function planeRideCost() {
  let londonPrice = '183';
  let parisPrice = '220';
  let commonPrice = '300';
  let answer = 0;

  while (typeof answer !== 'string') {
    answer = prompt('What is your destination?') ?? 0;
  }

  if (answer.toLowerCase() === 'london') {
    return (londonPrice + ' dollars')
  } else if (answer.toLowerCase() === 'paris') {
    return (parisPrice + ' dollars')
  } else {
    return (commonPrice + ' dollars')
  }
}

// console.log(planeRideCost()); // -> for 10 days = 1400

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the react-exercise.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the react-exercise. The react-exercise costs $40 everyday.
// If the user rents a react-exercise for more than 10 days, they get a 5% discount.
// The function should return the total price of the react-exercise rental.
function rentalCarCost() {
  let numberOfDays = 0;
  let totalPrice;
  let price = 40;

  while (numberOfDays === 0 ) {
        answer = prompt('How long do you need a react-exercise?');
        isNaN(Number(answer)) ? 0 : numberOfDays = Number(answer);
      }

  if (numberOfDays > 10) {
    const discount = (numberOfDays * price) * 0.05
    totalPrice = (numberOfDays * price) - discount
    return totalPrice;
  }
  totalPrice = numberOfDays * price;
  return totalPrice;
}

// console.log(rentalCarCost()); // -> for 10 days = 400

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The react-exercise cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()
function totalVacationCost() {
  const hotelPrice = hotelCost();
  const planePrice = planeRideCost();
  const carPrice = rentalCarCost();

  console.log(`The hotel cost: $${hotelPrice}, the plane tickets cost: ${planePrice}, the car cost: $${carPrice}.`);

  const totalCost = hotelPrice + carPrice + parseInt(planePrice);

  console.log(`Total vacation cost: $${totalCost}`);
}

totalVacationCost();
// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.


// 🌟 Exercise 5 : Users
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the second <li> of the second <ul>.
// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
// Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).


// 🌟 Exercise 6 : Change The Navbar
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>


// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).


// Exercise 7 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.