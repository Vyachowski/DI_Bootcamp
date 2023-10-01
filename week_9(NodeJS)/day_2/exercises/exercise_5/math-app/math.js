// 🌟 Exercise 5: Creating And Using A Custom Module
// Instructions:
// Create a directory named math-app.
// Inside the math-app directory, open a terminal and run npm init to initialize a new Node.js project. Follow the prompts to set up your project.
// Install the lodash package, a utility library, by running npm install lodash in the terminal.
// Create a file named math.js inside the math-app directory.

// In math.js, define a simple custom module that exports functions for addition and multiplication.

// Create a file named math.js in the same directory.
import _ from "lodash";
// In math.js, require the lodash package and the custom math module.

function sum(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

export { sum, multiply, _ };
// Use the exported functions from the math module and the utility functions from the lodash package to perform calculations.
// Run math.js using Node.js and verify that the calculations are correct.