// Create another file named app.js.
// In app.js, import the functions from the fileManager.js module.
const { readFile, writeFile } = require('./fileManager');
// Create a file “Hello World.txt” containing the sentence “Hello World !! “
writeFile('Hello World !! ', 'Hello World.txt',);
// Create a file “Bye World.txt” containing the sentence “Bye World !! “
writeFile('Bye World !! ', 'Bye World.txt');
// Use the imported functions to read the content of the “Hello World.txt” text file
// and then write to the “Bye World.txt” with the content “Writing to the file”.
const fileContent = readFile('Hello World.txt');
writeFile( fileContent, 'Bye World.txt');
// Run app.js and verify that the file reading and writing operations are successful.