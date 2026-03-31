from extract import extraction
from transform import transformation 
from load import loading

def main():
    raw_data = extraction()

    pokemon_table, pokemon_stats, pokemon_types = transformation(raw_data)

    loading(pokemon_table, pokemon_stats, pokemon_types)

if __name__ == "__main__":
    main()