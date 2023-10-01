const nameInputElement = document.querySelector('#first_name');
const lastNameInputElement = document.querySelector('#last_name');
const submitButtonElement = document.querySelector('#submit');
const formElement = document.querySelector('#form');
const paragraph = document.querySelector('.appended-text');
let paragraphText = paragraph.textContent;


formElement.addEventListener('submit', (event) => {
  event.preventDefault();
  const firstName = nameInputElement.value;
  const lastName = lastNameInputElement.value;
  const appendedText = JSON.stringify({'name': firstName, 'Last Name': lastName}, null , 2);
  paragraph.textContent = appendedText;
})