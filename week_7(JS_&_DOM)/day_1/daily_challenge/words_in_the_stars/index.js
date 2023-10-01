// Daily Challenge: Words In The Stars
// Prompt the user for several words (separated by commas)
let answer = '';

const star = '*';
const lineStarter = star + ' ';
const lineFinisher = ' ' + star;
const borderline = lineStarter.repeat(9);

while (answer.length === 0) {
  answer = prompt('Give me several words separated by comma, please');
}
// Put the words into an array
const arrayOfWords = answer.split(',');
const longestWordLength = (arrayOfWords.sort((a, b) => b.length - a.length))[0].length;

// Console.log the words one per line, in a rectangular frame as seen below
const resultWords = arrayOfWords.map((el) => lineStarter + el + lineFinisher);

console.log(resultWords);
// Check out the Hints and Requirements below.
// For example, if the user gives you:
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as: