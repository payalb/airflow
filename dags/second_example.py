from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}

def get_name():
    return 'Payal';

def greet(name, age):
    print(f'hello world, my name is {name}, age is {age}')

with DAG(
    dag_id = 'second_example',
    default_args= default_args,
    description="second example dag",
    start_date = datetime(2024, 6,10, 2),
    schedule_interval= '@daily'
) as dag:
    task1 = PythonOperator(
       task_id= 'greet',
       python_callable= greet,
       op_kwargs={'name': 'Payal','age':  39}
    )

    task2 = PythonOperator(
       task_id= 'get_name',
       python_callable= get_name
    )

    task1 >> task2