import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://localhost:8000/users')
      .then(res => res.json())
      .then(data => {
        setUsers(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  return (
    <div className="App">
      <h1>Lista de Usuarios</h1>
      {loading ? (
        <p>Cargando...</p>
      ) : (
        <ul>
          {users.map(user => (
            <li key={user.id}>
              <h3>{user.id}</h3>
              <strong>{user.name}</strong> - {user.email} - {user.password}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default App
