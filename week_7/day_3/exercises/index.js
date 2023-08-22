// 🌟 Exercise 1 : Change The Article
// Using a DOM property, retrieve the h1 and console.log it.
const headerElement = document.querySelector('h1');

// Using DOM methods, remove the last paragraph in the <article> tag.
const articleElement = document.querySelector('article');
articleElement.removeChild(articleElement.lastElementChild);

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
const headerTwoElement = document.querySelector('h2');
headerTwoElement.addEventListener('click', () => headerTwoElement.style.backgroundColor = 'red');

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
const headerThreeElement = document.querySelector('h3');
headerThreeElement.addEventListener('click', () => headerThreeElement.style.display = 'none');

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
function makeBold() {
  const allParagraphs = document.querySelectorAll('p');
  allParagraphs.forEach((el) => el.style.fontWeight = '700');
}

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
headerElement.setAttribute('onmouseover', "this.style.fontSize='32px';");
headerElement.setAttribute('onmouseout', "this.style.fontSize='24px';");
// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)


// 🌟 Exercise 2 : Change The Article
// Retrieve the form and console.log it.
const formElement = document.querySelector('form');
console.log(formElement);

// Retrieve the inputs by their id and console.log them.
const fnameInput = document.querySelector('#fname');
const lnameInput = document.querySelector('#lname');
console.log(fnameInput);
console.log(lnameInput);

// Retrieve the inputs by their name attribute and console.log them.
const fnameInputAlt = document.getElementsByName('firstname');
const lnameInputAlt = document.getElementsByName('lastname');
console.log(fnameInputAlt);
console.log(lnameInputAlt);

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ? -> to prevent a default bhaviour and handle it manually
// get the values of the input tags,
// make sure that they are not empty,
formElement.addEventListener('submit', (event) => {
  event.preventDefault();
  const firstName = fnameInput.value;
  const lastName = lnameInput.value;
  if (firstName.length === 0) {
    alert('Do you have a name, sir? Please try again');
  }
  if (lastName.length === 0) {
    alert('Do you have a lastname, sir? Please try again');
  }

  // create an li per input value
  const firstNameListItem = document.createElement('li');
  const lastNameListItem = document.createElement('li');
  firstNameListItem.textContent = firstName;
  lastNameListItem.textContent = lastName;
  const listAnswers = document.querySelector('.usersAnswer');

  // then append them to a the <ul class="usersAnswer"></ul>, below the form.
  listAnswers.append(firstNameListItem, lastNameListItem);
});

// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>


// In the JS file:

// Declare a global variable named allBoldItems.
let allBoldItems;

// Create a function called getBoldItems() that takes no parameter. 
// This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
function getAllBoldItems() {
  const boldTestingGround = document.querySelector('.boldTestingGround');
  allBoldItems = boldTestingGround.querySelectorAll('strong');
}

// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight() {
  getAllBoldItems();
  allBoldItems.forEach((el) => el.style.color = 'blue');
}

// Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.
function returnItemsToDefault() {
  getAllBoldItems()
  allBoldItems.forEach((el) => el.style.color = 'black');
}

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout 
// (ie. when the mouse pointer is moved out of the paragraph). Look at this example
const paragraphWithBold = document.querySelector('.boldTestingGround');
paragraphWithBold.addEventListener('mouseover', highlight);
paragraphWithBold.addEventListener('mouseout', returnItemsToDefault);



// Exercise 5 : Event Listeners
const transformerElement = document.getElementById("transformer");

transformerElement.addEventListener("click", function () {
  this.style.backgroundColor = "orange";
  this.style.border = '3px solid red';
  this.style.paddingBlock= '30px';
});

transformerElement.addEventListener("mouseover", function () {
  this.style.textAlign = "center";
});

transformerElement.addEventListener("mouseout", function () {
  this.style.textAlign = "right";
});
