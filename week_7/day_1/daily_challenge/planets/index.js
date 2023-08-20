// Daily Challenge: Planets
// Create an array which value is the planets of the solar system
const planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'];
const planetList = document.querySelector('.listPlanets');

// For each planet in the array, create a <div> using createElement. This div should have a class named "planet"
const planetElements = [];
planets.forEach(el => planetElements.push(document.createElement('div')));
planetElements.forEach(element => element.classList.add('planet'));

// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color)
let index = 0;
planetElements.forEach(element => {element.classList.add(planets[index]); index++;})

// Finally append each div to the <section> in the HTML (presented below)
planetElements.forEach(element => planetList.appendChild(element));