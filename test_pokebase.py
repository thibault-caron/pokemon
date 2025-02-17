import pokebase as pb

import pokebase as pb


def get_pokemon_info(pokemon_name):
    # Initialisation du dictionnaire qui contiendra les informations
    pokemon_info = {}

    try:
        # Récupérer les données du Pokémon
        pokemon = pb.pokemon(pokemon_name)
        species = pb.pokemon_species(pokemon_name)

        # Ajouter le nom du Pokémon
        pokemon_info['name'] = pokemon.name.capitalize()

        # Ajouter les types
        pokemon_info['types'] = [t.type.name.capitalize() for t in pokemon.types]

        # Ajouter les statistiques : Attaque, Défense, PV
        stats = {stat.stat.name: stat.base_stat for stat in pokemon.stats}
        pokemon_info['stats'] = stats

        # Ajouter les évolutions
        evolution_chain_id = species.evolution_chain.id  # Utilisation correcte de l'ID
        evolution_chain = pb.evolution_chain(evolution_chain_id)

        evolutions = []
        evolution = evolution_chain.chain
        while evolution:
            evolutions.append(evolution.species.name.capitalize())
            evolution = evolution.evolves_to[0] if evolution.evolves_to else None
        pokemon_info['evolutions'] = evolutions

        # Ajouter les images
        images = {
            'official_artwork': f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon.id}.png",
            'front_sprite': f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon.id}.png",
            'shiny_sprite': f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{pokemon.id}.png"
        }
        pokemon_info['images'] = images

    except Exception as e:
        print(f"Erreur lors de la récupération des données pour {pokemon_name}: {e}")
        return None

    return pokemon_info


# Entrée utilisateur pour choisir un Pokémon
pokemon_name = input("Entrez le nom du Pokémon: ").lower()

# Récupérer les informations du Pokémon
pokemon_data = get_pokemon_info(pokemon_name)

# Afficher les informations du Pokémon
if pokemon_data:
    print("\nInformations sur le Pokémon:")
    for key, value in pokemon_data.items():
        if key == 'images':
            print(f"\nImages:")
            for img_type, img_url in value.items():
                print(f"  {img_type.capitalize()}: {img_url}")
        else:
            print(f"{key.capitalize()}: {value}")
