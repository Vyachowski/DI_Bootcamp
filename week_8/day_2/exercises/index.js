// 🌟 Exercise 1: Comparison
// Instructions:
// Create a function called compareToTen(num) that takes a number as an argument.
// The function should return a Promise:
// the promise resolves if the argument is less than or equal to 10
// the promise rejects if argument is greater than 10.


function compareToTen(num) {
  const promise = new Promise((resolve, reject) => {
    if (num <= 10) {
      resolve(num);
    } else {
      reject('Number is more then ten');
    }
  });
  return promise;
};

// Test:
// In the example, the promise should reject
compareToTen(15)
  .then(result => console.log(result)) 
  .catch(error => console.log(error)) // -> Number is more then 10

// //In the example, the promise should resolve
compareToTen(8)
  .then(result => console.log(result)) // -> 8
  .catch(error => console.log(error))


// 🌟 Exercise 2: Promises
// Instructions:
// Create a promise that resolves itself in 4 seconds and returns a “success” string.
function successInFourSeconds() {
  const promise = new Promise((resolve, reject) => {
    resolve(setTimeout(() => {
      console.log('And here is a success!!!');
    }, 4000));
  });
  return promise;
};

successInFourSeconds();

// 🌟 Exercise 3: Resolve & Reject
// Instructions:
// Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
// Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”
const promiseResolved = Promise.resolve(3);
promiseResolved.then((value) => console.log(value));

const promiseRejected = Promise.reject('Sorry I will be always rejected no matter why');
promiseResolved.catch((error) => console.log(error));
// Exercise 4: Quizz - Not Mandatory
// Follow this tutorial and do the quizz until the page called “a few tricks with promises”.
