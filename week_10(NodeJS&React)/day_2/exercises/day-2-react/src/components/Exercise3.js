import React from "react";
import logo from '../logo.svg'
import './Exercise.css';

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial"
};
class Exercise extends React.Component{
  render () {
    return (
      <section>
        <h1 style={{color: "red", backgroundColor: "lightblue"}}>Header!</h1>
        <h1 style={style_header}>Header!</h1>
        <p className="para">I am a paragraph</p>
        <a href="#form">Scroll to form</a>
        <form id="form">
          <input type="search"/>
        </form>
        <img src={logo} alt="Something..."/>
        <ul>
          <li>First</li>
          <li>Second</li>
        </ul>
      </section>
    )
  }
}

export default Exercise;