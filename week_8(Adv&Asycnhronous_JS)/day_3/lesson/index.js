const paragraph = document.querySelector('.chuck-joke');
const button = document.querySelector('.joke-button');

button.addEventListener('click', () => {
  fetch('https://api.chucknorris.io/jokes/random')
    .then((response) => response.json())
    .then((data) => paragraph.textContent = JSON.stringify(data.value))
})