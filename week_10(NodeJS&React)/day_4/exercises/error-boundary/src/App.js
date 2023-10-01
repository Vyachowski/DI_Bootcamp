import ErrorBoundary from './components/ErrorBoundary';
import './App.css';
import {Component} from "react";

class BuggyCounter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 0
    };
  }

  handleClick = () => {
    this.setState(prevState => ({
      counter: prevState.counter + 1
    }));

    if (this.state.counter === 4) {
      throw new Error('I crashed!');
    }
  };

  render() {
    return <div onClick={this.handleClick}>{this.state.counter}</div>;
  }
}

function App() {
  return (
    <div className="App">
      <h1>Error Boundary Simulations</h1>
      <h2>Simulation 1:</h2>
      <ErrorBoundary>
        <BuggyCounter />
        <BuggyCounter />
      </ErrorBoundary>

      <h2>Simulation 2:</h2>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>

      <h2>Simulation 3:</h2>
      <BuggyCounter />
    </div>
  );
}

export default App;
