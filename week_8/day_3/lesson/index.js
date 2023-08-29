const paragraph = document.querySelector('.chuck-joke');

fetch('https://api.chucknorris.io/jokes/random')
    .then((response) => response.json())
    .then((data) => paragraph.textContent = JSON.stringify(data.value));