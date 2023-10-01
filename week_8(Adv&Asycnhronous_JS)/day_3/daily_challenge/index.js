// Daily Challenge: Gifs
// Instructions:
// Use this Giphy API Random documentation. Use this API Key : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
// In the HTML file, add a form, containing an input and a button.
// This input is used to fetch gif depending on a specific category.
// In the JS file, create a program to fetch one random gif depending on the search of the user
// (ie. If the search is “sun”, append on the page one gif with a category of “sun”).
// The gif should be appended with a DELETE button next to it.
// Hint : to find the URL of the gif, look for the sub-object named “images” inside the data you receive from the API.
// Allow the user to delete a specific gif by clicking the DELETE button.
// Allow the user to remove all of the GIFs by clicking a DELETE ALL button.

const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const form = document.querySelector("#form");
const categoryInput = document.querySelector("#input");
const deleteAllButton = document.querySelector("#deleteAll");
const gifContainer = document.querySelector("#container");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const category = categoryInput.value.trim();
  if (category === "") return;

  try {
    const gifData = await fetchRandomGif(category);
    appendGif(gifData, category);
  } catch (error) {
    console.error("Error fetching GIF:", error);
  }
});

deleteAllButton.addEventListener("click", () => {
  gifContainer.innerHTML = "";
});

async function fetchRandomGif(category) {
  const apiUrl = `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${category}`;
  const response = await fetch(apiUrl);
  const data = await response.json();
  return data;
}

function appendGif(gifData, category) {
  const gifUrl = gifData.data.images.downsized.url;
  const gifElement = document.createElement("div");
  gifElement.innerHTML = `
    <img src="${gifUrl}" alt="${category}">
    <button class="deleteButton">Delete</button>
  `;
  gifContainer.appendChild(gifElement);

  const deleteButton = gifElement.querySelector(".deleteButton");
  deleteButton.addEventListener("click", () => {
    gifContainer.removeChild(gifElement);
  });
}