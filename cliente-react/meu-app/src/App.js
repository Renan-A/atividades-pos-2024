import React from 'react';
import './App.css';
import PokemonForm from './components/PokemonForm';
import PokemonSprites from './components/PokemonSprites';
import ErrorMessage from './components/ErrorMessage';

function App() {
  return (
    <div className="App">
      <h1>Pokémon Finder</h1>
      <PokemonForm />
    </div>
  );
}

export default App;
