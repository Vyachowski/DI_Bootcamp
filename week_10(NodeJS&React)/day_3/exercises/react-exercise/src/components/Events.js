import { useState } from "react";

export default function Events() {
  // keyDown exercise
  const [inputValue, setInputValue] = useState('');
  const clickMe = () => {
    alert('I was clicked!');
  }

  const handleKeyDown = (e) => {
    if (e.keyCode === 13) {
      alert(`You pressed Enter with the value: ${inputValue}`);
    }
    setInputValue(e.target.value); // Without last symbol? Why?
  }

  // toggleOn exercise
  const [isToggleOn, setToggleStatus] = useState(true);

  function toggleButton(e) {
    setToggleStatus(!isToggleOn);
  }

  return(
    <div style={{textAlign: 'center'}}>
      <div style={{textAlign: 'center'}}>
        <p>
          <button type='button' onClick={clickMe}>Click me!</button>
        </p>
        <p>
          <input type="text" onKeyDown={handleKeyDown} placeholder='Type something and press enter'/>
        </p>
      </div>
      <p style={{textAlign: 'center'}}>
        <button type={"button"} onClick={toggleButton}>{isToggleOn ? 'On': 'Off'}</button>
      </p>
    </div>
  )
}
