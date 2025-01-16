import React, { useState } from 'react';
import PokemonSprites from './PokemonSprites';
import ErrorMessage from './ErrorMessage';

function PokemonForm() {
  const [pokemon, setPokemon] = useState('');
  const [sprites, setSprites] = useState(null);
  const [error, setError] = useState('');

  const fetchPokemon = async (e) => {
    e.preventDefault();
    setError('');
    setSprites(null);

    try {
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`);
      if (!response.ok) {
        throw new Error('Pokémon not found!');
      }
      const data = await response.json();
      setSprites({
        front: data.sprites.front_default,
        back: data.sprites.back_default,
      });
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <form onSubmit={fetchPokemon}>
        <input
          type="text"
          placeholder="Enter Pokémon name"
          value={pokemon}
          onChange={(e) => setPokemon(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
      {error && <ErrorMessage message={error} />}
      {sprites && <PokemonSprites front={sprites.front} back={sprites.back} />}
    </div>
  );
}

export default PokemonForm;
