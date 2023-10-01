import './App.css';
import {Component} from "react";
class FormComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: '',
      lastName: '',
      age: '',
      gender: '',
      destination: 'none',
      nutsFree: false,
      lactoseFree: false,
      vegan: false
    };
  }
  handleChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  }

  handleChangeCheckboxes = (event) => {
    const { name } = event.target;
    this.setState((prevState) => ({ [name]: !prevState[name] }));
    console.log(this.state[name]); // Ask Daniel what's going on
  }

  // handleSubmit = (event) => {
  //   event.preventDefault();
  //   const { firstName, lastName, age, gender, destination, nutsFree, lactoseFree, vegan } = this.state;
  //
  //   const queryString = `firstName=${firstName}&lastName=${lastName}&age=${age}&gender=${gender}&destination=${destination}&nutsFree=${nutsFree}&lactoseFree=${lactoseFree}&vegan=${vegan}`;
  //   window.location.href = `${queryString}`;
  // }

  render() {
    return (
      <>
        <form className='form' action={'#'} method={'get'}> {/* onSubmit={this.handleSubmit}*/}
          <h1 className={'form-name'}>Sample form</h1>
          <fieldset className={'user-info-fieldset'}>
            <legend>User's info</legend>
            <input className='input' type="text" value={this.state.firstName} onChange={this.handleChange} placeholder='First Name' name={'firstName'}/>
            <input className='input' type="text" value={this.state.lastName} onChange={this.handleChange} placeholder='Last Name'  name={'lastName'}/>
            <input className='input' type="text" value={this.state.age} onChange={this.handleChange} placeholder='Age' name={'age'}/>
            <div className={'gender-selection'}>
              <label htmlFor={'maleGender'}>
                <input className='input' type="radio" value={'male'} onChange={this.handleChange} name={'gender'} id={'maleGender'}/>
                Male
              </label>
              <label htmlFor={'femaleGender'}>
                <input className='input' type="radio" value={'female'} onChange={this.handleChange} name={'gender'} id={'femaleGender'}/>
                Female
              </label>
            </div>
          </fieldset>
          <div className={'destination-fieldset'}>
            <legend>Select your destination</legend>
            <label htmlFor="destination">
              <select name="destination" id="destination" onChange={this.handleChange}>
                <option value="None">Select an option</option>
                <option value="Japan">Japan</option>
                <option value="Japan!">I think Japan</option>
                <option value="Japan!!">The only option – Japan</option>
              </select>
            </label>
          </div>
          <fieldset className={'restrictions-fieldset'}>
            <legend>Dietary restrictions</legend>
            <label htmlFor={'nutsFree'}>
              <input className='input' type="checkbox" onChange={this.handleChangeCheckboxes} name={'nutsFree'} id={'nutsFree'}/>
              Nuts free
            </label>
            <label htmlFor={'lactoseFree'}>
              <input className='input' type="checkbox" onChange={this.handleChangeCheckboxes} name={'lactoseFree'} id={'lactoseFree'} />
              Lactose free
            </label>
            <label htmlFor={'vegan'}>
              <input className='input' type="checkbox" onChange={this.handleChangeCheckboxes} name={'vegan'} id={'vegan'}/>
              Vegan
            </label>
          </fieldset>
          <button className={'send-button'} type={'submit'}>Submit</button>
        </form>
        <section className={'result'}>
          <h2>Entered information</h2>
          <p>Your first name: {this.state.firstName}</p>
          <p>Your last name: {this.state.lastName}</p>
          <p>Your age: {this.state.age}</p>
          <p>Your gender: {this.state.gender}</p>
          <p>Your destination: {this.state.destination}</p>
          <p>Your dietary restrictions: <br/><br/>
            <span>**Nuts free {this.state.nutsFree ? 'Yes': 'No'}</span><br/>
            <span>**Lactose free {this.state.lactoseFree ? 'Yes': 'No'}</span><br/>
            <span>**Vegan {this.state.vegan ? 'Yes': 'No'}</span><br/>
          </p>
        </section>
      </>
    );
  }
}
function App() {
  return (
    <FormComponent/>
    )
}

export default App;
