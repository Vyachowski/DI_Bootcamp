// 🌟 Exercise 6 : Change The Navbar
// Using Javascript, in the <div>, change the value of the id attribute 
// from navBar to socialNetworkNavigation, using the setAttribute method.
const navbarElement = document.querySelector('#navBar');
const listElement = document.querySelector('ul');
navbarElement.setAttribute('id','socialNetworkNavigation');

// First, create a new <li> tag (use the createElement method)
const newListElement = document.createElement('li');

// Create a new text node with “Logout” as its specified text
const newTextElement = document.createTextNode('Logout');
// newListElement.textContent = 'Logout';

// Append the text node to the newly created list node (<li>)
newListElement.append(newTextElement);

// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
listElement.appendChild(newListElement);

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
const firstListElement = listElement.firstElementChild;
const lastListElement = listElement.lastElementChild;

const firstListElementText = firstListElement.textContent;
const lastListElementText = lastListElement.textContent;

console.log(firstListElementText);
console.log(lastListElementText);

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.