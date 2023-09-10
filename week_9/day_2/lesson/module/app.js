const axios = require('axios');
const info = async() => {
  try {
    return await axios.get('https://jsonplaceholder.typicode.com/users');
  }
  catch(e) {
    console.log(e);
  }
}

info().then(data => console.log(data));

module.exports = info;