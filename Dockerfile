FROM apache/airflow:2.9.2

# Compulsory to switch parameter
ENV PIP_USER=false
#python venv setup
RUN python3 -m venv /opt/airflow/venv1
COPY requirements.txt /requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel      
RUN  /opt/airflow/venv1/bin/pip install -r /requirements.txt
ENV PIP_USER=true
