@echo off
SET "AIRFLOW_VERSION=3.0.2"

REM Extract the version of Python you have installed. If you're currently using Python 3.11 you may want to set this manually as noted above, Python 3.11 is not yet supported.
SET "PYTHON_VERSION=3.12.10"

SET "CONSTRAINT_URL=https://raw.githubusercontent.com/apache/airflow/constraints-%AIRFLOW_VERSION%/constraints-%PYTHON_VERSION%.txt"
REM For example this would install 2.7.1 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.8.txt

echo "Install with the following command:"
echo "pip install "apache-airflow==%AIRFLOW_VERSION%" --constraint "%CONSTRAINT_URL%""