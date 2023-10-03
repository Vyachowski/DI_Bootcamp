import './App.css';
import {Component} from "react";

class Part1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    }
  }
  async componentDidMount() {
    const response = await fetch('http://localhost:3001/api/hello');
    const data = await response.text();
    this.setState({data})
  }

  render() {
    return <h1>Part 1: {this.state.data}</h1>
  }
}

class Part2 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null,
      input: '',
    }
  }

  handleChange(event) {
    const value = event.target.value;
    this.setState({input: value})
  }

  async handleSubmit(event) {
    event.preventDefault();
    const requestData = this.state.input;
    const requestObject = {text: requestData}
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // Указываем, что отправляем JSON данные
      },
      body: JSON.stringify(requestObject) // Преобразуем объект в JSON строку
    };

    const data = await fetch('http://localhost:3001/api/world', requestOptions);
    const response = await data.json();
    this.setState({ data: response.text });
  }

  render() {
    return (
      <section>
        <h1>Part 2: Post to server</h1>
        <form action="#" method={'post'} onSubmit={async (event) => await this.handleSubmit(event)}>
          <input type={'text'} value={this.state.input} onChange={(event) => this.handleChange(event)}></input>
          <button type={'submit'}>Submit</button>
        </form>
        {this.state.data && (
          <p>I received your POST request. This is what you sent me: {this.state.data}</p>
        )}
      </section>
    )
  }
}
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Part1 />
        <Part2 />
      </header>
    </div>
  );
}

export default App;
