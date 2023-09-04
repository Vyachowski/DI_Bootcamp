const { greeting, hello } = require('./greeting');
const fetchUsersData = require('./userAPI');

console.log("greetings =>", greeting('People'));
console.log("Hello =>", hello('People'));

fetchUsersData.then(data => console.log(data));