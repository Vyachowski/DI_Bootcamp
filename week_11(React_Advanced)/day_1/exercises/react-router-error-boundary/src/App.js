import './App.css';
import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
   console.log(error, info);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback;
    }

    return this.props.children;
  }
}

class ErrorComponent extends React.Component {
  constructor(props) {
    super(props);
  }

  handleClick = () => {
    throw new Error("Congrats, you have an error!!!");
  };

  render() {
    return (
      <div onClick={this.handleClick}>
        Пока все нормально...
      </div>
    )
  }
}

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Мое React приложение</h1>
        <ErrorBoundary fallback={<p>Something went wrong</p>}>
          <ErrorComponent />
        </ErrorBoundary>
      </div>
    );
  }
}

export default App;
