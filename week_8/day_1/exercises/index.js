// 🌟 Exercise 1: Location
// Analyze the code below. What will be the output?
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }
// const {name, location: {country, city, coordinates: [lat, lng]}} = person;
// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat};

// ANSWER: I am John Doe from Vancouver, Canada. 49.2827


// 🌟 Exercise 2: Display Student Info
// Instructions
function displayStudentInfo(objUser){
    const {first, last} = objUser;
    return `Your full name is ${first} ${last}`;
}

// Output: 
console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));

