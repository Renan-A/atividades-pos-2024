import React from 'react';

function PokemonSprites({ front, back }) {
  return (
    <div>
      <img src={front} alt="Front sprite" />
      <img src={back} alt="Back sprite" />
    </div>
  );
}

export default PokemonSprites;
