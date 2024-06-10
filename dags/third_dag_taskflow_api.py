from airflow.decorators import task, dag
from datetime import datetime, timedelta

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}

@dag(dag_id='example_using_decorators', default_args= default_args, start_date=datetime(2024, 6,10, 2),schedule_interval= '@daily')
def hello_world_etl():
    
    @task()
    def get_name(ti):
        ti.xcom_push(key= "first_name", value = "payal")
        ti.xcom_push(key= "last_name", value = "bansal")
    
    @task()
    def get_age(ti):
        ti.xcom_push(key= "age", value = 39)

    @task()
    def greet(ti):
        first_name = ti.xcom_pull(task_ids= 'get_name', key= "first_name")
        last_name = ti.xcom_pull(task_ids= 'get_name', key = "last_name")
        age = ti.xcom_pull(task_ids= 'get_age', key = "age")
        print(f'hello world, my name is {first_name} {last_name}, age is {age}')

    get_age()
    get_name();
    greet();

greet_dag = hello_world_etl()