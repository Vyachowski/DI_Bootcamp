const axios = require('axios');

async function fetchPosts() {
  return (await axios.get('https://jsonplaceholder.typicode.com/posts/1')).data;
}

module.exports = fetchPosts;