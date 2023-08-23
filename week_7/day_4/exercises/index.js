// 🌟 Exercise 1 : Colors
// Instructions
// Using this array :
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
colors.forEach((element, index) => console.log(`${index + 1}# choice is ${element}`));
// Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
colors.some(element => element === 'Violet') ? console.log('Yeah') : console.log('No');
// Hint : Use the array methods taught in class. Look at the lesson Array Methods.


// 🌟 Exercise 2 : Colors #2
// Instructions
// Using these arrays :
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];
// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
colors.slice(0, ordinal.length).forEach((element, index) => console.log(`${index + 1}${ordinal[index]} choice is ${element}`));
// Hint : Use the array methods taught in class and ternary operator.


// Exercise 3 : Analyzing
// Instructions
// Analyze these pieces of code before executing them. What will be the outputs ?
// ------1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);

// ------2------
// const country = "USA";
// console.log([...country]);

// ------Bonus------
// let newArray = [...[,,]];
// console.log(newArray);


// 🌟 Exercise 4 : Employees
// Instructions
// Using this array:
const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];
// Using the map() method, push into a new array the firstname of the user and a welcome message. You should get an array that looks like this :
// const welcomeStudents = ["Hello Bradley", "Hello Chloe", "Hello Jonathan", "Hello Michael", "Hello Robert", "Hello Wes", "Hello Zach"]
const welcomeStudents = [];
users.map((user) => welcomeStudents.push(`Hello ${user.firstName}`));
// console.log(welcomeStudents); // -> ['Hello Bradley', 'Hello Chloe', 'Hello Jonathan', 'Hello Michael', 'Hello Robert', 'Hello Wes', 'Hello Zach']

// 2. Using the filter() method, create a new array, containing only the Full Stack Residents.
const fullStackDevs = users.filter((user) => user.role === 'Full Stack Resident');
// console.log(fullStackDevs); // -> { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' }...
// 3. Bonus : Chain the filter method with a map method, to return an array containing only the lastName of the Full Stack Residents.
// console.log(users.filter((user) => user.role === 'Full Stack Resident').map((user) => user.lastName)); // -> ['Bouley', 'Alnaji', 'Hajek']


// 🌟 Exercise 5 : Star Wars
// Instructions
// Using this array 
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// Use the reduce() method to combine all of these into a single string.
const notSoEpic = epic.reduce((acc, word) => acc + ' ' + word);
// console.log(notSoEpic); // -> a long time ago in a galaxy far far away

// 🌟 Exercise 6 : Employees #2
// Instructions
// Using this object:

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];
// Using the filter() method, create a new array, containing the students that passed the course.
// Bonus : Chain the filter method with a forEach method, to congratulate the students with their name and course name 
// (ie. “Good job Jenner, you passed the course in Information Technology”, “Good Job Marco you passed the course in Robotics” ect…)
const passedStudents = students.filter(student => student.isPassed);
// console.log(passedStudents); // -> {Ray...}...
// passedStudents.forEach((student) => console.log(`Congratulions, ${student.name}`)); // -> Congratulions, Ray...