import './App.css';
import {useState} from "react";

function App() {
  const [languages, setLanguages] = useState([
    {name: "Php", votes: 0},
    {name: "Python", votes: 0},
    {name: "JavaScript", votes: 0},
    {name: "Java", votes: 0}
  ])

  function increaseVote(number) {
    const updatedLanguages = [...languages];
    updatedLanguages[number].votes += 1;
    setLanguages(updatedLanguages);
  }

  return (
    <div className="App">
      <ul className='languages-list'>
        <li className='language-item'>
          <span className='votes'>{languages[0].votes}</span>
          <span className='language-name'>Php</span>
          <button className='votes-total' type='button' onClick={() => increaseVote(0)}>Click here</button>
        </li>
        <li className='language-item'>
          <span className='votes'>{languages[1].votes}</span>
          <span className='language-name'>Python</span>
          <button className='votes-total' type='button' onClick={() => increaseVote(1)}>Click here</button>
        </li>
        <li className='language-item'>
          <span className='votes'>{languages[2].votes}</span>
          <span className='language-name'>JavaScript</span>
          <button className='votes-total' type='button' onClick={() => increaseVote(2)}>Click here</button>
        </li>
        <li className='language-item'>
          <span className='votes'>{languages[3].votes}</span>
          <span className='language-name'>Java</span>
          <button className='votes-total' type='button' onClick={() => increaseVote(3)}>Click here</button>
        </li>
      </ul>
    </div>
  );
}

export default App;
