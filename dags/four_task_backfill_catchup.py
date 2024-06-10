from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}
#if today is 10th june, dag would be execuetd for all backdates.

with DAG(
    dag_id = 'fourth_dag_catchup_backfill',
    default_args= default_args,
    description="fourth example dag",
    start_date = datetime(2024, 6,1), #scheduled in past
    schedule_interval= '@daily',
    catchup= True
) as dag:
    task1 = BashOperator(
        task_id= 'first_task',
        bash_command="echo hello world"
    )

