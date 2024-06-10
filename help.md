1) Install python https://www.python.org/downloads/release/python-3124/
Add python to path : C:\Users\Payal\AppData\Local\Programs\Python\Python312
C:\Users\Payal\AppData\Local\Microsoft\WindowsApps
C:\Users\Payal\AppData\Local\Programs\Python\Python312\Scripts
2) Check version installed: python --version
3) create python environment: python -m venv py_env # py_env is the folder name
pip3 install -U pip virtualenv
cd py_env
.\Scripts\activate
pip install apache-airflow
set AIRFLOW_HOME = /airflow
airflow db init

docker

https://airflow.apache.org/docs/apache-airflow/2.0.2/docker-compose.yaml
docker-compose up airflow-init
docker-compose up
docker-compose up airflow-init

Used to manage complex workflows (sequence of tasks), written in python.
DAG: dynamic acyclic graph

task: unit of work within a dag (node in dag graph, written in python. dependencies in tasks)
operator: what gets done by task [bash operator, python operator.. custom operator]

execution date: logical date time, when dag ran
task instance: run of task at specific point of time.
dag run: instantiation of dag containing task instances that run for a specific date.

Task lifecycle: 
queued, running, success, failed, up_for_retry, up_for_reschedule, upstream_failed, skipped, scheduled, no_status, shutdown, removed

  AIRFLOW__CORE__LOAD_EXAMPLES: 'false'

  In dags folder create first example.


xcom: to share value between tasks. Max size: 48 kb

task flow api: 

catchup: True: if today is 10th june, dag would be execuetd for all backdates.
airflow dags backfill -s 2024-06-01 -e 2024-06-10 <dag_id>

schedule interval -> datetime.timedelta, cron expression

cron expression: minute, hour, day (month), month , day(week)
crontab.guru

Airflow connect to postgres: Admin -> Connections 

postgres host should be service name in dockerfile.
or host.docker.internal

docker-compose down -v # also removing volumes.

https://airflow.apache.org/docs/apache-airflow/1.10.5/macros.html

install dependencies to airflow docker container: Image extending or Image customizing
Add requirements.txt
create dockerfile to extend airflow image with added dependencies.
docker build . --tag extending_airflow:latest
in docker-compose refer to the new dockerfile image name.

https://www.youtube.com/watch?v=K9AnJ9_ZAXE