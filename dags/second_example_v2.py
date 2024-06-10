from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}

def get_name(ti):
    ti.xcom_push(key= "first_name", value = "payal")
    ti.xcom_push(key= "last_name", value = "bansal")

def greet(age, ti):
    first_name = ti.xcom_pull(task_ids= 'get_name', key= "first_name")
    last_name = ti.xcom_pull(task_ids= 'get_name', key = "last_name")
    print(f'hello world, my name is {first_name} {last_name}, age is {age}')

with DAG(
    dag_id = 'second_example_v2',
    default_args= default_args,
    description="second example dag",
    start_date = datetime(2024, 6,10, 2),
    schedule_interval= '@daily'
) as dag:
    task1 = PythonOperator(
       task_id= 'greet',
       python_callable= greet,
       op_kwargs={'age':  39}
    )

    task2 = PythonOperator(
       task_id= 'get_name',
       python_callable= get_name
    )

    task2 >> task1