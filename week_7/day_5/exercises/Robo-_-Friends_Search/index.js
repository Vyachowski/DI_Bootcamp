// Mini-Project - Robo-Friends Search
const robots = [
  {
    id: 1,
    name: 'Leanne Graham',
    username: 'Bret',
    email: 'Sincere@april.biz',
    image: 'https://robohash.org/1?200x200'
  },
  {
    id: 2,
    name: 'Ervin Howell',
    username: 'Antonette',
    email: 'Shanna@melissa.tv',
    image: 'https://robohash.org/2?200x200'
  },
  {
    id: 3,
    name: 'Clementine Bauch',
    username: 'Samantha',
    email: 'Nathan@yesenia.net',
    image: 'https://robohash.org/3?200x200'
  },
  {
    id: 4,
    name: 'Patricia Lebsack',
    username: 'Karianne',
    email: 'Julianne.OConner@kory.org',
    image: 'https://robohash.org/4?200x200'
  },
  {
    id: 5,
    name: 'Chelsey Dietrich',
    username: 'Kamren',
    email: 'Lucio_Hettinger@annie.ca',
    image: 'https://robohash.org/5?200x200'
  },
  {
    id: 6,
    name: 'Mrs. Dennis Schulist',
    username: 'Leopoldo_Corkery',
    email: 'Karley_Dach@jasper.info',
    image: 'https://robohash.org/6?200x200'
  },
  {
    id: 7,
    name: 'Kurtis Weissnat',
    username: 'Elwyn.Skiles',
    email: 'Telly.Hoeger@billy.biz',
    image: 'https://robohash.org/7?200x200'
  },
  {
    id: 8,
    name: 'Nicholas Runolfsdottir V',
    username: 'Maxime_Nienow',
    email: 'Sherwood@rosamond.me',
    image: 'https://robohash.org/8?200x200'
  },
  {
    id: 9,
    name: 'Glenna Reichert',
    username: 'Delphine',
    email: 'Chaim_McDermott@dana.io',
    image:'https://robohash.org/9?200x200'
  },
  {
    id: 10,
    name: 'Clementina DuBuque',
    username: 'Moriah.Stanton',
    email: 'Rey.Padberg@karina.biz',
    image:'https://robohash.org/10?200x200'
  }
  ];

// Part I: Display robots
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
  card.appendChild(cardImageWrapper);
  card.appendChild(cardTitle);
  card.appendChild(cardEmail);

  // Getting the result
  return card;

  // // Test Ground
  // const list = document.querySelector('.robo-list');
  // list.appendChild(card);
}

function displayRobots(list) {
  if (typeof list !== 'object') {
    alert('Should be an object');
  }
  const section = document.querySelector('.robo-list');

}

// Part II: Filter robots
function filterRobots(query) {
  if (query.length === 0 || typeof query !== 'string') {
    return robots;
  }
  robots.forEach((robot) => robot.name.toLowerCase());
  const filteredRobotsList = robots.filter((robot) => robot.name.includes(query));
  return filteredRobotsList;
}

function normalizeQuery() {
  const inputValue = document.getElementById("robosearch").value;
  const normalizedQuery = inputValue.replace(/\s+/g, " ").trim().toLowerCase();
  return normalizedQuery;
}