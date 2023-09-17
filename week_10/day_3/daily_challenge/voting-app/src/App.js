import './App.css';
import {useState} from "react";

function App() {
  const [languages, setLanguages] = useState([
    {name: "Php", votes: 0},
    {name: "Python", votes: 0},
    {name: "JavaScript", votes: 0},
    {name: "Java", votes: 0}
  ])

  function increaseVote(languageName) {
    setLanguages((previousVariant) => {
      const updatedLanguages = [...previousVariant];
      const language = updatedLanguages.find(
        (lang) => lang.name === languageName
      );
      if (language) {
        language.votes += 1;
        console.log(updatedLanguages);
      }
      return updatedLanguages;
    });
  }

  return (
    <div className="App">
      <ul className='languages-list'>
        <li className='language-item'>
          <span className='votes'>{languages[0].votes}</span>
          <span className='language-name'>Php</span>
          <button className='votes-total' type='button' onClick={() => increaseVote('Php')}>Click here</button>
        </li>
        <li className='language-item'>
          <span className='votes'>{languages[1].votes}</span>
          <span className='language-name'>Python</span>
          <button className='votes-total' type='button' onClick={() => increaseVote('Python')}>Click here</button>
        </li>
        <li className='language-item'>
          <span className='votes'>{languages[2].votes}</span>
          <span className='language-name'>JavaScript</span>
          <button className='votes-total' type='button' onClick={() => increaseVote('JavaScript')}>Click here</button>
        </li>
        <li className='language-item'>
          <span className='votes'>{languages[3].votes}</span>
          <span className='language-name'>Java</span>
          <button className='votes-total' type='button' onClick={() => increaseVote('Java')}>Click here</button>
        </li>
      </ul>
    </div>
  );
}

export default App;
