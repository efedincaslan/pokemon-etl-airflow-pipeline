from extract import extraction
import logging 


def transformation(data):
    
    try:
        

        pokemon_table =[]
        pokemon_stats = []
        pokemon_types = []



        for i in data:
            pokemon_id = i['id']
            name = i['name']
            height = i['height']
            weight = i['weight']

            formatted = {
            'pokemon_id' : pokemon_id,
            'name' : name,
            'height' : height,
            'weight' : weight
                    }
            pokemon_table.append(formatted)
            #start of stats table transformation


            stats = i['stats']
            for x in stats:
                base_stat = x.get('base_stat')
                stat = x.get('stat')
                stat_name = stat.get('name')
                formatted_stats = {
                'pokemon_id' : pokemon_id,
                'base_stat' : base_stat,
                'stat_name' : stat_name
                    }
                pokemon_stats.append(formatted_stats)

            # start of type table
            types = i['types']
            for w in types:
                typeofpokemon = w.get('type')
                element = typeofpokemon.get('name')
                formatted_type = {
                        'pokemon_id' : pokemon_id,
                        'type_name' : element
                    }
                pokemon_types.append(formatted_type)
        return pokemon_table, pokemon_stats, pokemon_types
    except Exception as e:
        logging.error(f'error occured{e}')
        return pokemon_table, pokemon_stats, pokemon_types
    
