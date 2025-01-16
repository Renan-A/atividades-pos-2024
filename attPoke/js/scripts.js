const frontSprite = document.getElementById("front-sprite");
const backSprite = document.getElementById("back-sprite");
const pokemonName = document.getElementById("pokemon-name");
const pokemonNumber = document.getElementById("pokemon-number");
const pokemonType = document.getElementById("pokemon-type");
const pokemonAbility = document.getElementById("pokemon-ability");
const pokemonAverage = document.getElementById("pokemon-average");

let currentPokemon = 1; 

async function fetchPokemon(pokemon) {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error("Pokémon não encontrado");
        }
        const data = await response.json();

        updatePokemonInfo(data);
    } catch (error) {
        alert(error.message);
    }
}

function updatePokemonInfo(data) {
    frontSprite.src = data.sprites.front_default || "img/placeholder.png";
    backSprite.src = data.sprites.back_default || "img/placeholder.png";

    pokemonName.textContent = capitalizeFirstLetter(data.name);
    pokemonNumber.textContent = data.id;
    pokemonType.textContent = data.types.map((type) => capitalizeFirstLetter(type.type.name)).join(", ");
    pokemonType.style.backgroundColor = getTypeColor(data.types[0].type.name);
    pokemonAbility.textContent = capitalizeFirstLetter(data.abilities[0].ability.name);

    const stats = data.stats.map((stat) => stat.base_stat);
    const average = stats.reduce((a, b) => a + b, 0) / stats.length;
    pokemonAverage.textContent = average.toFixed(1);

    currentPokemon = data.id;
}

function searchByName() {
    const name = document.getElementById("name-search").value.trim();
    if (name) fetchPokemon(name);
}

function searchByNumber() {
    const number = parseInt(document.getElementById("number-search").value);
    if (number && number > 0) fetchPokemon(number);
}

function previousPokemon() {
    if (currentPokemon > 1) fetchPokemon(--currentPokemon);
}

function nextPokemon() {
    if (currentPokemon < 1025) fetchPokemon(++currentPokemon);
}

function capitalizeFirstLetter(string
) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}   