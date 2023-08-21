function insertRow() {
  // Create column
  const newColumn = document.createElement('td');
  const newSecondColumn = document.createElement('td');

  newColumn.textContent = 'Row cell';
  newSecondColumn.textContent = 'Row cell';

  // Create row
  const newRow = document.createElement('tr');

  // Add two columns to row
  const tableElement = document.querySelector('#sampleTable');
  newRow.appendChild(newColumn);
  newRow.appendChild(newSecondColumn);
  
  // Add rows to table
  tableElement.appendChild(newRow);
}
