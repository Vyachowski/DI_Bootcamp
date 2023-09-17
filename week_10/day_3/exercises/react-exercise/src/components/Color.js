import {useEffect, useState} from "react";

export default function Color() {
  const [favoriteColor, setColor] = useState('red');

  useEffect(() => {
    setColor('Yellow');
    alert('useEffect reached')
  }, []);

  function changeButtonColorToBlue() {
    setColor('Blue');
  }

  return(
    <div style={{textAlign: 'center'}}>
      <h1>My favorite color is {favoriteColor}</h1>
      <button type='button' onClick={changeButtonColorToBlue}>Change color to blue</button>
    </div>
  )
}
