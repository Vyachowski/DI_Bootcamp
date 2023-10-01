let rowNumber = 3;

function insertRow() {
  // Create column
  const newColumn = document.createElement('td');
  const newSecondColumn = document.createElement('td');

  newColumn.textContent = `Row${rowNumber} cell1`;
  newSecondColumn.textContent = `Row${rowNumber} cell2`;

  // Create row
  const newRow = document.createElement('tr');

  // Add two columns to row
  const tableElement = document.querySelector('#sampleTable');
  newRow.append(newColumn, newSecondColumn);
  
  // Add rows to table
  tableElement.append(newRow);

  // Row Number increment
  rowNumber += 1;
}

// Exercise 2 – Change the button
const button = document.querySelector('#jsstyle');

function invisibleButton() {
  button.textContent = 'Stop please';
  button.style.color = 'red';
  button.style.border = 0;
  button.style.backgroundColor = 'transparent';
}
