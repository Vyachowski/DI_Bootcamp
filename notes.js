const test = [2, 4, 5, 6, 7];

function recursiveSum(numbers) {
  if (numbers.length === 0) {
    return 0;
  }
  return numbers.pop() + recursiveSum(numbers);
}

console.log(recursiveSum(test));

const test2 = "Hello, World!";

function reverseString(str) {
  if (str.length == 1) {
    return str;
  }
  return str[str.length - 1] + reverseString(str.substr(0, str.length - 1));
}

console.log(reverseString(test2));

const test3 = 2;
const test4 = 2;

function powerOf(base, exponent) {
  if (exponent === 1) {
    return base;
  }
  return base * powerOf(base, exponent - 1);
}

console.log(powerOf(test3, test4));
