from airflow import DAG
from airflow.utils.dates import days_ago

from operators.postgres import DataTransferPostgres
from operators.utils import source_table_list

DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
    "depends_on_past": True,
}

with DAG(
    dag_id='pg-data-flow',
    default_args=DEFAULT_ARGS,
    schedule_interval='*/1 * * * *',
    catchup=True,
    max_active_runs=1,
    tags=['data-flow'],
) as dag1:
    # task1 = DataTransferPostgres(
    #     config={'table': 'public.customer'},
    #     query='select * from customer',
    #     task_id='customer',
    #     source_pg_conn_str="host='postgres_a' port=5432 dbname='database_a' user='postgres' password='postgres'",
    #     target_pg_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'",
    #     pg_meta_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'"
    # )

    dump = {
        table: DataTransferPostgres(
            config={'table': f'public.{table}'},
            query=f'select * from {table}',
            task_id=f'{table}',
            source_pg_conn_str="host='postgres_a' port=5432 dbname='database_a' user='postgres' password='postgres'",
            target_pg_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'",
            pg_meta_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'"
        )
        for table in source_table_list("host='postgres_a' port=5432 dbname='database_a' user='postgres' password='postgres'")
    }
