import logo from './logo.svg';
import hongKong from './carouselImages/hongkong.jpeg'
import macao from './carouselImages/macao.webp'
import japan from './carouselImages/japan.webp'
import lasVegas from './carouselImages/lasvegas.webp'
import './App.css';
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';


function App() {
  return (
    <div className="carousel-container" style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
    }}>
      <Carousel width={500} dynamicHeight={true} >
        <div>
          <img src={hongKong} alt={"Hong-Kong"}/>
          <p className="legend">Hong-Kong</p>
        </div>
        <div>
          <img src={macao} alt={"Macao"} />
          <p className="legend">Macao</p>
        </div>
        <div>
          <img src={japan} alt={"Japan"} />
          <p className="legend">Japan</p>
        </div>
        <div>
          <img src={lasVegas} alt={"Las-Vegas"} />
          <p className="legend">Las-Vegas</p>
        </div>
      </Carousel>
    </div>
  );
}

export default App;
