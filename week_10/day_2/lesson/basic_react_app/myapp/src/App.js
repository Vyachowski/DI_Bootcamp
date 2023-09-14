import './App.css';
import User from "./components/User";
import users from './data.json'
function App() {
  return (
    <div className="App">
      <header className="App-header">
        {users.map((item) => {
          return <User name={item.name} email={item.email}/>
        })}
      </header>
    </div>
  );
}

export default App;
