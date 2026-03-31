CREATE SCHEMA IF NOT EXISTS pokemon_data;

CREATE TABLE IF NOT EXISTS pokemon_data.pokemon (
    pokemon_id INT PRIMARY KEY,
    name TEXT,
    height INT,
    weight INT
);

CREATE TABLE IF NOT EXISTS pokemon_data.pokemon_stats (
    pokemon_id INT,
    stat_name TEXT,
    base_stat INT,
    PRIMARY KEY (pokemon_id, stat_name)
);

CREATE TABLE IF NOT EXISTS pokemon_data.pokemon_types (
    pokemon_id INT,
    type_name TEXT,
    PRIMARY KEY (pokemon_id, type_name)
);