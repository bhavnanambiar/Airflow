from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from datetime import datetime
from airflow.operators.python import PythonOperator
import boto3

def file_present():
   print("file present")

with DAG(
   dag_id='s3_file_sensor_dag',
   start_date=datetime(2025, 1, 1),
   schedule_interval=None,
   catchup=False,
) as dag:
   wait_for_s3_file = FileSensor(
       task_id='wait_for_s3_file',
       filepath='s3://mybucket-awstest/sample3.json',
       fs_conn_id='s3_default',  # Connection ID for S3
       poke_interval=30,
       timeout=600,
       mode='poke',
   )

   print_file_present=PythonOperator(
      task_id='print_file_present',
      python_callable=file_present,

   )

   wait_for_s3_file >> print_file_present
