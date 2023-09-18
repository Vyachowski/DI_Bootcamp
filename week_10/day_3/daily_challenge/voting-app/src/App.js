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
    const updatedLanguages = [...languages];
    const lang = updatedLanguages.find((language) => language.name === languageName);
    if (lang) {
      lang.votes += 1;
    }
    setLanguages(updatedLanguages);
  }

  return (
    <div className="App">
      <ul className='languages-list'>
        {languages.map((language, index) => {
          return (<li key={index} className={'language-item language-item-' + index}>
            <span className='votes'>{language.votes}</span>
            <span className='language-name'>{language.name}</span>
            <button className='votes-total' type='button' onClick={() => increaseVote(language.name)}>Click here</button>
          </li>)
        })}
      </ul>
    </div>
  );
}

export default App;
