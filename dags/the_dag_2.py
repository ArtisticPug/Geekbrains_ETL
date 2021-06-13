from airflow import DAG
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.utils.dates import days_ago

from operators.statistics import WriteStatisticsOperator
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
    dag_id='pg-data-statistics',
    default_args=DEFAULT_ARGS,
    schedule_interval='@daily',
    catchup=True,
    max_active_runs=1,
    tags=['data-flow-statistics'],
) as dag1:
    # sensor = ExternalTaskSensor(
    #     task_id='customer_sensor',
    #     external_dag_id='pg-data-flow',
    #     external_task_id='customer'
    # )
    # statistics = WriteStatisticsOperator(
    #     task_id='customer_statistics',
    #     config={'table': 'public.customer'},
    #     pg_meta_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'",
    #     target_pg_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'"
    # )

    for table in source_table_list("host='postgres_a' port=5432 dbname='database_a' user='postgres' password='postgres'"):
        sensor = ExternalTaskSensor(
            task_id=f'sae_{table}',
            external_dag_id='pg-data-final',
            external_task_id=f'sae_{table}'
        )

        statistics = WriteStatisticsOperator(
            config={'table': f'sae.{table}'},
            task_id=f'{table}_statistics',
            pg_meta_conn_str="host='postgres_c' port=5432 dbname='database_c' user='postgres' password='postgres'",
            target_pg_conn_str="host='postgres_b' port=5432 dbname='database_b' user='postgres' password='postgres'"
        ) 
        
        sensor >> statistics
