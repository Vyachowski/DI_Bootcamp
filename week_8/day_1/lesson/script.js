let myObj = {
  name : "John",
  lastName : "Doe",
  age : 25,
  friends : ["Mark", "Lucie", "Ana"]
};

const valuesCount = Object.values(myObj).length;
const keyCount = Object.keys(myObj).length;
const entries = Object.entries(myObj);

console.log(`"Keys : ${keyCount}, Values : ${valuesCount}"`);

entries.forEach((value, index) => {
  console.log(`The ${index + 1} key is ${value[0]}`);
  console.log(`The ${index + 1} value is ${value[1]}`);
});