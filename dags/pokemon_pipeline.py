from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="pokemon_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_etl = BashOperator(
        task_id="run_pokemon_etl",
        bash_command="python /opt/airflow/etl/main.py",
    )