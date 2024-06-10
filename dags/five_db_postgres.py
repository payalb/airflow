from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}

with DAG(
    dag_id = 'five_postgres_example',
    default_args= default_args,
    description="first example dag",
    start_date = datetime(2024, 6,10, 2),
    schedule_interval= '@daily'
) as dag:
    task1 = PostgresOperator(
        task_id= 'create_postgres_table',
        postgres_conn_id = "connection1",
        sql = """
            create table if not exists dag_runs (dt date, dag_id character varying, primary key (dt, dag_id))
        """ 
    )

    task2 = PostgresOperator(
        task_id= 'delete_postgres_table',
        postgres_conn_id = "connection1",
        sql = """
            delete from dag_runs where dt = '{{ds}}' and dag_id =  '{{dag.dag_id}}';
        """ 
    )

    task3 = PostgresOperator(
        task_id= 'insert_postgres_table',
        postgres_conn_id = "connection1",
        sql = """
            insert into dag_runs (dt, dag_id) values ('{{ds}}', '{{dag.dag_id}}')
        """ 
    )

    task1 >> task2 >> task3


