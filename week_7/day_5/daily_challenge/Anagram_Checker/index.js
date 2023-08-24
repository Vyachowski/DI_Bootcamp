// Daily Challenge: Anagram
// Create a function that:
// – takes in two strings as two parameters
// – and returns a boolean that indicates whether or not the first string is an anagram of the second string.
function isAnagram(word1, word2) {
  // Normalizing array
  const lettersList1 = word1.trim().split('').map((letter) => letter.toLowerCase());
  const lettersList2 = word2.trim().split('').map((letter) => letter.toLowerCase());

  // Ordering letters
  const orderedLetters1 = lettersList1.toSorted().filter((letter) => letter !== ' ');
  const orderedLetters2 = lettersList2.toSorted().filter((letter) => letter !== ' ');

  // Returning to squence
  const normalizedSequence1 = orderedLetters1.join('');
  const normalizedSequence2 = orderedLetters2.join('');

  return (normalizedSequence1 === normalizedSequence2);
}

// Examples
console.log(isAnagram('mooo on', 'no ooom')); // -> True
console.log(isAnagram('Astronomer', 'Moon starer')); // -> True
console.log(isAnagram('School master', 'The classroom')); // -> True
console.log(isAnagram('The Morse Code', 'Here come dots')); // -> True

// Examples of false result
console.log(isAnagram('moon', 'bobeer')); // -> False
console.log(isAnagram('Astronomer', 'Moon starter')); // -> False
