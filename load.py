from transform import transformation
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy import text
import logging



def upsert_pokemon(engine, pokemon_table):
    query = text("""
        INSERT INTO pokemon_data.pokemon (pokemon_id, name, height, weight)
        VALUES (:pokemon_id, :name, :height, :weight)
        ON CONFLICT (pokemon_id)
        DO UPDATE SET
            name = EXCLUDED.name,
            height = EXCLUDED.height,
            weight = EXCLUDED.weight;
    """)

    with engine.begin() as conn:
        conn.execute(query, pokemon_table)


def upsert_stats(engine, pokemon_stats):
    query = text("""
        INSERT INTO pokemon_data.pokemon_stats (pokemon_id, stat_name, base_stat)
        VALUES (:pokemon_id, :stat_name, :base_stat)
        ON CONFLICT (pokemon_id, stat_name)
        DO UPDATE SET
            base_stat = EXCLUDED.base_stat;
    """)

    with engine.begin() as conn:
        conn.execute(query, pokemon_stats)

def upsert_types(engine, pokemon_types):
    query = text("""
        INSERT INTO pokemon_data.pokemon_types (pokemon_id, type_name)
        VALUES (:pokemon_id, :type_name)
        ON CONFLICT (pokemon_id, type_name)
        DO NOTHING;
    """)

    with engine.begin() as conn:
        conn.execute(query, pokemon_types)


load_dotenv()



def loading(pokemon_table, pokemon_stats, pokemon_types):
    
    user = os.getenv('db_user')
    password = os.getenv('db_pass')

    DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@postgres:5432/Pokedex"

    engine = create_engine(DATABASE_URL)

    # Verify connection (optional)
    try:
        with engine.connect() as connection:
            print("Database connected successfully!")
        
        
        upsert_pokemon(engine, pokemon_table)
        upsert_stats(engine, pokemon_stats)
        upsert_types(engine, pokemon_types)
        logging.info('Database updated succesfully')

    except Exception as ex:
        print(f"Connection failed: {ex}")

