const API_URL = 'https://pokeapi.co/api/v2/pokemon/';

export async function fetchPokemonData(pokemonName) {
    try {
        const response = await fetch(`${API_URL}${pokemonName}`);
        if (!response.ok) throw new Error('Pokémon not found');
        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
}
