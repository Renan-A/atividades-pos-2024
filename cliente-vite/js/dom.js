import { fetchPokemonData } from './wrapper.js';

const form = document.querySelector('#pokemon-form');
const frontSprite = document.querySelector('#front-sprite');
const backSprite = document.querySelector('#back-sprite');
const errorMessage = document.querySelector('#error-message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const pokemonName = document.querySelector('#pokemon-name').value.trim();

    try {
        const data = await fetchPokemonData(pokemonName.toLowerCase());
        frontSprite.src = data.sprites.front_default;
        backSprite.src = data.sprites.back_default;
        errorMessage.textContent = ''; // Limpa mensagens de erro
    } catch (error) {
        frontSprite.src = '';
        backSprite.src = '';
        errorMessage.textContent = error.message;
    }
});
