// Retrieve the div and console.log it
const containerElement = document.getElementById('container');
console.log(containerElement.textContent);

// Change the name “Pete” to “Richard”.
const listItems = document.querySelectorAll('li');
listItems.forEach(element => element.textContent === 'Pete' ?
   element.textContent = 'Richard' : null);

// Delete the second <li> of the second <ul>
const listElements = document.querySelectorAll('.list');
const secondList = listElements[1];
const secondElement = secondList.childNodes[3];
secondList.removeChild(secondElement);

// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)


// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
// Change the font size of the whole body.