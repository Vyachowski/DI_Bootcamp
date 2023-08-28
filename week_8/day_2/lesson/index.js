// – Create a function that takes in a single parameter and returns a new promise.
// – Using setTimeout, after 5000 milliseconds, the promise will either resolve or reject.
// – If the input is a string, the promise resolves with that same string uppercased.
// – If the input is anything but a string it rejects with that same input.
// – Use then to repeat the string twice use catch to console.log the error finally call a function that console.log ("congratulation")

function newFunction (parameter) {
  return new Promise((resolve, reject) => {
    setTimeout(()=> {
      if (typeof parameter === 'string') {
        resolve(parameter.toUpperCase())
      } else {
        console.log("rejects");
        reject('It is not a string')
      }
    }
    , 3000);
  });
}

newFunction('6')
    .then(parameter => console.log(parameter.repeat(2)))
    .catch((error) => ('Sorry, here is your error', error))
    .finally(()=> console.log('Finally it works!'));

newFunction(6)
    .then(parameter => console.log(parameter.repeat(2)))
    .catch((error) => console.log('Sorry, here is your error', error))
    .finally(()=> console.log('Finally it works!'));