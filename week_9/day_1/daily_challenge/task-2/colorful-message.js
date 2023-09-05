// Task 2: Using an NPM Module
// Inside the daily-challenge directory, open a terminal and run npm init to initialize a new Node.js project. Follow the prompts to set up your project.
// Install the chalk package by running npm install chalk in the terminal.
// Create a file named colorful-message.js.
// In colorful-message.js, require the chalk package and use it to create and display a colorful message in the terminal.
// Create another file named app.js.
// In app.js, require the colorful-message.js module and call the function you’ve written to display the colorful message.
// Run app.js using Node.js and see the colorful message.

import chalk from "chalk";

export default function displayColorfulMessage() {
  const colorfulMessage =
    chalk.bold.blue('This is a bold blue message!') + '\n' +
    chalk.rgb(255, 136, 0).underline('This is an underlined orange message!') + '\n' +
    chalk.bgCyan.white('This is a white message on a cyan background!') + '\n' +
    chalk.green('This is a green message!') + '\n' +
    chalk.red('This is a red message!') + '\n' +
    chalk.bold.magenta('This is a bold magenta message!') + '\n' +
    chalk.yellow('This is a yellow message!') + '\n' +
    chalk.cyan('This is a cyan message!') + '\n' +
    chalk.white.bgBlue('This is a blue message on a white background!') + '\n' +
    chalk.bgRed.yellow('This is a yellow message on a red background!') + '\n' +
    chalk.inverse('This is an inverted message!') + '\n' +
    chalk.strikethrough('This is a strikethrough message!') + '\n' +
    chalk.bold.gray('This is a bold gray message!') + '\n' +
    chalk.bgMagenta.white('This is a white message on a magenta background!');

  console.log(colorfulMessage);
}
