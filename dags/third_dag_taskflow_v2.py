from airflow.decorators import task, dag
from datetime import datetime, timedelta

default_args= {
    'owner' : 'payalb',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2)
}

@dag(dag_id='example_using_decorators_v2', default_args= default_args, start_date=datetime(2024, 6,10, 2),schedule_interval= '@daily')
def hello_world_etl():
    
    @task(multiple_outputs= 'true')
    def get_name():
        return {
            "first_name": 'payal',
            "last_name": 'bansal'
        }
    
    @task()
    def get_age():
        return 39;

    @task()
    def greet(first_name, last_name, age):
        print(f'hello world, my name is {first_name} {last_name}, age is {age}')

    age = get_age()
    name_dict = get_name();
    greet( first_name= name_dict["first_name"], last_name= name_dict["last_name"] ,age = age);

greet_dag = hello_world_etl()