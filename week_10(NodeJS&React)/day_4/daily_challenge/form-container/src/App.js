import './App.css';
import {Component} from "react";
class FormComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  handleChange(event) {
    const data = event.target.value;
    console.log(data);
  }
}
function App() {
  return (
    <div></div>
  );
}

export default App;
