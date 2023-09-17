import { useState, useEffect } from 'react'
import Garage from "./Garage";
export default function Car(props) {
  const [color, setColor] = useState('nothing');
  useEffect(() => {
    setColor('yellow');
  }, []);
  return (
    <div>
      <h1 style={{textAlign: "center"}}>This car is {color}, {props.model}</h1>
      <Garage size={props.size}></Garage>
    </div>
  )
}