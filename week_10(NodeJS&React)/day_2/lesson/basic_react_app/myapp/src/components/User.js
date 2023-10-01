const User = (props) => {
  return(
    <div>
      <h2>{props.name}</h2>
      <p>{props.email}</p>
      <p>{props.username}</p>
    </div>
  )
}

export default User;