// Part I
setTimeout(function() {
  alert('Hello World');
}, 2000);

// Part II
setTimeout(function() {
  var container = document.getElementById('container');
  var paragraph = document.createElement('p');
  paragraph.textContent = 'Hello World';
  container.appendChild(paragraph);
}, 2000);

// Part III
var interval = setInterval(function() {
  var container = document.getElementById("container");
  var paragraphCount = container.getElementsByTagName("p").length;

  if (paragraphCount < 5) {
      var newParagraph = document.createElement("p");
      newParagraph.textContent = "Hello World";
      container.appendChild(newParagraph);
  } else {
      clearInterval(interval);
  }
}, 2000);

var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", function() {
  clearInterval(interval);
});
