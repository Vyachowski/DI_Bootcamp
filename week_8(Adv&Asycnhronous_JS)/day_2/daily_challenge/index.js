// Daily Challenge: Play With Words
// Instructions
// 1rst Daily Challenge
// – Create two functions. Each function should return a promise.
// – The first function called makeAllCaps(), takes an array of words as an argument
// – If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
//   else, reject the promise with a reason.
// – The second function called sortWords(), takes an array of words uppercased as an argument
// – If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
//   else, reject the promise with a reason.
function makeAllCaps(words) {
  const promise = new Promise((resolve, reject)=> {
    if (words.length >=4 && words.every((value) => typeof value === 'string')) {
      resolve(words);
    } else {
      reject('Proper array is not provided')
    }
  });
  return promise;
};

function sortWords(words) {
  const promise = new Promise((resolve) => {
    const sortedWords = words.toSorted();
    resolve(sortedWords);
  });
  return promise;
}


// // Test:
// //in this example, the catch method is executed
// makeAllCaps([1, "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// //in this example, the catch method is executed
// makeAllCaps(["apple", "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// //in this example, you should see in the console, 
// // the array of words uppercased and sorted
// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
//       .catch(error => console.log(error))


// 2nd Daily Challenge
const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`
// Create three functions. The two first functions should return a promise.
// The first function is named toJs():
// – this function converts the morse json string provided above to a morse javascript object
// – if the morse javascript object is empty, throw an error (use reject) else return the morse javascript object (use resolve)
function toJS(JSONString) {
  const promise = new Promise((resolve, reject) => {
    if (JSONString.length === 0) {
      reject('Sorry, it is not a JSON string')
    } else {
      resolve(JSON.parse(JSONString));
    }
  });
  return promise;
};

// The second function called toMorse(morseJS), takes one argument: the new morse javascript object
function toMorse(morseDict) {
  const answer = prompt('Give me a word, or a sentece, please:').trim().toLowerCase();
  const answerByLetters = answer.split('');
  const morsesKeys = Object.keys(morseDict);
  const isStringValid = answerByLetters.every((letter) => morsesKeys.includes(letter));

  const promise = new Promise((resolve, reject) => {
    if (isStringValid) {
      const morseSequence = answerByLetters.map((letter) => morseDict[letter]);
      resolve(morseSequence);
    } else {
      const error = answerByLetters.find((letter) => (!morsesKeys.includes(letter)))
      reject(`String is not valid for morse alphabet – The problem is ${error}`);
    }
  });

  return promise;
};

// This function asks the user for a word or a sentence.
// – if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
// – else return an array with the morse translation of the user’s word.
// – if the user enters the word "Hello", the promise resolves with this value ["....", ".", ".-..", ".-..","---"]
// – if the user entered the word "¡Hola!", the promise rejects because the character "¡" doesn't exist in the morse javascript object


// The third function called joinWords(morseTranslation), takes one argument: the morse translation array
// this function joins the morse translation by using line break and display it on the page (ie. On the DOM)
function joinWords(morseString) {
  const morseText = morseString.join('<br>');
  // Variant with a console.log
  // console.log(morseText);

  // Variant with a dom modifying
  const paragraphElement = document.createElement('p');
  paragraphElement.innerHTML = morseText;
  console.log(paragraphElement);
  document.body.append(paragraphElement);
};

toJS(morse)
.then((dict) => toMorse(dict))
.then((string) => joinWords(string))
.catch(error => console.log(error));
// Chain the three functions.
// Example:
// "Hello" gives you
// ....
// .
// .-..
// .-..
// ---