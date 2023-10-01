import { useState } from "react";

export default function Phone() {
  const userPhone = {
    brand: "Samsung",
    model: "Galaxy S20",
    color: "black",
    year: 2020
  }

  const [phone, setPhone] = useState(userPhone);

  const changeColor = () => {
    userPhone.color = 'blue';
    setPhone(userPhone);
  }

  return(
    <div style={{textAlign: 'center'}}>
      <h1>My phone is {phone.brand}</h1>
      <p>It is {phone.color} {phone.model} from {phone.year}</p>
      <button type={'button'} onClick={changeColor}>Change color</button>
    </div>
  )
}
