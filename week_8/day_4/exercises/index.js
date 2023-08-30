// Instructions
// You should use this API: https://www.swapi.tech/ to get the data and update it “randomly” in your website by clicking a button.
//     Note: The API contains 83 different characters
//
// Create your HTML file, and add the relevant elements.
//
//     In your JS file, create your functions :
//     to retrieve the elements from the DOM.
//     to get the data from the API (star wars characters).
// to display the info on the DOM: the name, height, gender, birth year, and home world of the character.
//
//     Display the data using AJAX. Make sure to display a loading message as follows:
//     You can use any of these animation icons for the loading message.
//     Fontawesome link :
//     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css

const fetchButton = document.querySelector(".fetch-button");
const loading = document.querySelector(".loading");
const characterInfo = document.querySelector(".character");
const nameElement = document.getElementById("name");
const heightElement = document.getElementById("height");
const genderElement = document.getElementById("gender");
const birthYearElement = document.getElementById("birth-year");
const homeWorldElement = document.getElementById("home-world");

fetchButton.addEventListener("click", getRandomCharacter);

async function getRandomCharacter() {
  loading.style.display = "block";
  characterInfo.style.display = "none";
  const randomNumber = () => Math.floor(Math.random() * 93);

  try {
    const response = await fetch(`https://www.swapi.tech/api/people/${randomNumber()}`);
    const data = await response.json();
    const character = data.result.properties;

    nameElement.textContent = character.name;
    heightElement.textContent = character.height;
    genderElement.textContent = character.gender;
    birthYearElement.textContent = character.birth_year;

    const homeworldResponse = await fetch(character.homeworld);
    const homeworldData = await homeworldResponse.json();
    homeWorldElement.textContent = homeworldData.result.properties.name;

    loading.style.display = "none";
    characterInfo.style.display = "block";
  } catch (error) {
    console.error("Error fetching data:", error);
    loading.style.display = "none";
  }
}
