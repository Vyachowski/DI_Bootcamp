export default function UserFavoriteAnimals(props) {
  return (
    <ul>
      {props.favAnimals.map((animal, index) => <li key={index}>{animal}</li>)}
    </ul>
  )
}