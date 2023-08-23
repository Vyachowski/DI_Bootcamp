let client = 'John';
// client = 'Betty';

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    // totalPrice : "35$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.
const displayGroceries = () => groceries.fruits.forEach(element => {console.log(element)});
displayGroceries();

// Create another arrow function named cloneGroceries.
const cloneGroceries = () => {
  const user = client;
  const shopping = groceries;
};
// In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
// Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ?

// ANSWER: ANSWER: No, it will not be changed. Primitive values copies values, not references.

// In the function, create a variable named shopping that is equal to the groceries variable.
// Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?

// ANSWER: Yes, it will be changed, because objects copies by reference, it means new object points at the same position in the memory.

// Change the value of the paid key to false. Will we also see this modification in the shopping object ? Why ?

// Invoke the cloneGroceries function.