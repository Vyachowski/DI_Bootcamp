import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from "./components/userFavoriteAnimals";
import Exercise from "./components/Exercise3";

function App() {
  const myElement = <h1>I Love JSX!</h1>;
  const sum = 5 + 5;

  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  };
  return (
    // First exercise
    <div className="App">
        <p>
          Hello, World!
        </p>
      <p>
        {myElement}
        React is {sum} times better with JSX
      </p>
      {/*Second exercise*/}
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <UserFavoriteAnimals favAnimals={user.favAnimals} />
      <Exercise></Exercise>
    </div>

  );
}

export default App;
