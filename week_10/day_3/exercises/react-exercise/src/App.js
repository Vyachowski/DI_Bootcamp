import './App.css';
import Car from "./components/Car";

function App() {
  const carInfo = {name: "Ford", model: "Mustang"}
  return (
    <Car model={carInfo.model} size={'small'}></Car>
  );
}

export default App;
