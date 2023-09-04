// 🌟 Exercise 3: File Management Using CommonJS Syntax
// Instructions:
// Create a file named todo.js.
// Inside todo.js, define a module that exports functions for reading and writing files.
// Export functions named readFile and writeFile.
// Implement the readFile function to read the content of a specified file using the fs module.
const { readFileSync, writeFileSync} = require("node:fs");

function readFile(filePath) {
  let fileContent;
  try {
    fileContent = readFileSync(filePath, 'utf-8');
  } catch (e) {
    console.log(e);
  }
  return fileContent;
}

function writeFile(fileContent, filePath) {
  try {
      writeFileSync(filePath, fileContent);
  } catch (e) {
    console.log(e);
  }
  console.log('File was written successfully!')
}
// Implement the writeFile function to write content to a specified file using the fs module.
module.exports = { readFile, writeFile };