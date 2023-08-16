// Instructions:
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *
const starsNumber = 6;
const star = '* ';

// Solution 1
for (let i = 1; i <= starsNumber; i++) {
  console.log(star.repeat(i));
}

// Solution 2
for (let i = 1; i <= starsNumber; i++) {
  let starsRow = [];

  for (let j = 1; j <= i; j++) {
    starsRow.push(star);
  }

  console.log(starsRow.join(''));
}