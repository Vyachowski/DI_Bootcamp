import './App.css';
import Car from "./components/Car";
import Events from "./components/Events";
import Phone from "./components/Phone";
import Color from "./components/Color";

function App() {
  const carInfo = {name: "Ford", model: "Mustang"}
  return (
    <section>
      <Car model={carInfo.model} size={'small'}></Car>
      <Events></Events>
      <Phone></Phone>
      <Color></Color>
    </section>
  );
}

export default App;
