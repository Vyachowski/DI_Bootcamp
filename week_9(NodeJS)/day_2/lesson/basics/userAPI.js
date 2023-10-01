async function fetchUsersData() {
  const data = await fetch('https://jsonplaceholder.typicode.com/users');
  return await data.json();
}

module.exports = fetchUsersData();