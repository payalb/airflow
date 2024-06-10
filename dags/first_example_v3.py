from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}

with DAG(
    dag_id = 'first_example_v3',
    default_args= default_args,
    description="first example dag v3",
    start_date = datetime(2024, 6,10, 2),
    schedule_interval= '@daily' 
) as dag:
    task1 = BashOperator(
         task_id= 'first_task',
        bash_command="echo hello world"
    )

    task2 = BashOperator(
         task_id= 'second_task',
        bash_command="echo executed after task 1"
    )

    task3 = BashOperator(
         task_id= 'third_task',
        bash_command="echo executed after task 1, parallel to task 2"
    )

task1 >> task2
task1 >> task3

#same as adding task2 and task3 as a downstream to task1

# task1 >> [task2, task3]