import fs from 'node:fs';

// const data = fs.readFileSync('users.json', "utf-8");
// console.log(data);


fs.readFile("users.json", "utf-8", (data , err) => {
  if(err) return console.log(err);
  console.log(data);
});

data;