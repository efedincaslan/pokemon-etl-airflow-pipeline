import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO)

def fetch_pokemon_detail(pokemon):

    detail = pokemon.get("url")
    name = pokemon.get("name")

    logging.info(f"Fetching {name} from {detail}")

    try:
        response = requests.get(detail, timeout=12)

        if response.status_code == 200:
            logging.info("End point call successful")
            return response.json()

        else:
            logging.error(f"Failed to fetch {detail}")
            return None

    except Exception as e:
        logging.error(f"Error fetching {detail}: {e}")
        return None
    
def extraction():
    raw_data = []
    try:
        url = "https://pokeapi.co/api/v2/pokemon"
        limit = 100
        offset = 0
        while True:
            params = {'limit' : limit, 'offset' : offset}
            
            logging.info(f"Fetching page with offset {offset}")
            
            response = requests.get(url, params=params, timeout=12)

            if response.status_code != 200:
                logging.error(f'status code error {response.status_code}')
                break
            else:
                

                data = response.json() 
                results = data.get('results')

                if not results:
                    logging.info('no more results - pagination finished')
                    break
                
                
                with ThreadPoolExecutor(max_workers=10) as executor:

                    responses = executor.map(fetch_pokemon_detail, results)

                    for r in responses:
                        if r:
                            raw_data.append(r)
                    else:
                        logging.error(f"failed to fetch")

                offset += limit
                    
        return raw_data    
               
    except Exception as e:
        logging.error(f'Error : {e}')
        return raw_data