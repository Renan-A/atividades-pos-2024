import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [artistas, setArtistas] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/artistas/')
      .then(response => {
        setArtistas(response.data);
      })
      .catch(error => {
        console.error('Houve um erro ao pegar os artistas!', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Artistas</h1>
      <ul>
        {artistas.map(artista => (
          <li key={artista.id}>{artista.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
