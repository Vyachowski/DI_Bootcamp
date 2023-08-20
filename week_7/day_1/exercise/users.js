// Retrieve the div and console.log it
const containerElement = document.getElementById('container');
console.log(containerElement.textContent);

// Change the name “Pete” to “Richard”.
const listItems = document.querySelectorAll('li');
listItems.forEach(element => element.textContent === 'Pete' ?
   element.textContent = 'Richard' : null);

// Delete the second <li> of the second <ul>
const listElements = document.querySelectorAll('.list');
const firstList = listElements[0];
const secondList = listElements[1];
const secondElement = secondList.childNodes[3];
secondList.removeChild(secondElement);

// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)
listElements.forEach(elements => elements.firstElementChild.textContent = 'Slava The King of JS');


// Add a class called student_list to both of the <ul>'s
listElements.forEach(element => element.classList.add('student_list'));

// Add the classes university and attendance to the first <ul>
firstList.classList.add('university', 'attendance');


// Add a “light blue” background color and some padding to the <div>
containerElement.setAttribute('style', 'text-align: center; background-color: lightblue; padding-block: 20px;')

// Do not display the <li> that contains the text node “Dan”
// (the last <li> of the first <ul>)
listItems.forEach(element => element.textContent === 'Dan' ?
element.setAttribute('style', 'display: none;') : null);
// Add a border to the <li> that contains the text node “Richard”
// (the second <li> of the <ul>)
listItems.forEach(element => element.textContent === 'Richard' ?
element.setAttribute('style', 'border: 25px orange solid; padding: 20px;') : null);
// Change the font size of the whole body.
document.body.setAttribute('style', 'font-size: 25px;')

// Bonus: If the background color of the div is “light blue”, 
// alert “Hello x and y” (x and y are the users in the div).
const names = [];
listItems.forEach(elements => names.push(elements.textContent));
const uniqueNames = [...new Set(names)].slice(0, 2);
console.log(uniqueNames);
if (containerElement.style.backgroundColor === 'lightblue') {
  alert(`Hello: ${uniqueNames.join(', ')}`)
}