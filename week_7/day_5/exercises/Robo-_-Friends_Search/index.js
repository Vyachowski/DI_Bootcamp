// Mini-Project - Robo-Friends Search

// Displaying all robots
const filteredList = filterRobots('');
displayRobots(filteredList);

// Adding event listener to input
const inputElement = document.getElementById('robosearch');
inputElement.addEventListener('input', updateFilteredRobots);

// Function for updating list
function updateFilteredRobots() {
  removeAllChildNodes(document.querySelector('.robo-list'));
  const normalizedQuery = normalizeQuery();
  console.log(normalizedQuery);
  const filteredList = filterRobots(normalizedQuery);
  displayRobots(filteredList);
}

// Function for removing child nodes
function removeAllChildNodes(parent) {
  while (parent.firstChild) {
      parent.removeChild(parent.firstChild);
  }
};

/* Part I: Display robots */

function createCard(obj) {
  // Creating card
  const card = document.createElement('li');
  card.classList.add('card');
  // Creating card image-wrapper
  const cardImageWrapper = document.createElement('div');
  cardImageWrapper.classList.add('card-image-wrapper');
  // Creating card image
  const cardImage = document.createElement('img');
  cardImage.setAttribute('src', obj.image);
  cardImage.classList.add('card-image');
  // Creating card title
  const cardTitle = document.createElement('h2');
  cardTitle.textContent = obj.name;
  cardTitle.classList.add('card-title');
  // Creating card email
  const cardEmail = document.createElement('p');
  cardEmail.textContent = obj.email;
  cardEmail.classList.add('card-email');

  // Appending nodes
  cardImageWrapper.appendChild(cardImage);
  card.append(cardImageWrapper, cardTitle, cardEmail);

  // Getting the result
  return card;
}

function displayRobots(list) {
  // Checking if argument fits
  if (typeof list !== 'object') {
    alert('Should be an object');
  }

  // Getting parent container
  const listElement = document.querySelector('.robo-list');

  // Creating cards
  const cards = list.map((robot) => createCard(robot));

  // Appending cards
  cards.forEach((card) => listElement.appendChild(card));
}

/* Part II: Filter robots */

function filterRobots(query) {
  // Checking query
  if (typeof query !== 'string') {
    return robots;
  }

  // Filtering array with query
  const filteredRobotsList = robots.filter((robot) =>
  robot.name.toLowerCase().includes(query));
  console.log(filteredRobotsList);
  // Getting result
  return filteredRobotsList;
}

function normalizeQuery() {
  const inputValue = document.getElementById("robosearch").value;
  const normalizedQuery = inputValue.replace(/\s+/g, " ").trim().toLowerCase();
  return normalizedQuery;
}