// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.
const sentence = 'The movie is not that bad, I like it';
// const sentence = 'This dinner is bad !'
// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).
const wordNot = sentence.indexOf('not'); console.log(wordNot); // -> 13
// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).
const wordBad = sentence.indexOf('bad'); console.log(wordBad); // -> 22
// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
if (wordBad > wordNot && wordNot > 0) {
  const sentenceLength = sentence.length;
  const wordBadLength = 'bad'.length;
  const newSentenceFirstPart = sentence.substring(0, wordNot);
  const newSentenceLastPart= sentence.substring(wordBad + wordBadLength);
  const newSentence = newSentenceFirstPart + ' good' + newSentenceLastPart;
  console.log(newSentence);
} else {
  console.log(sentence);
}
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.