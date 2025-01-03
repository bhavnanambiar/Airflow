from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def process_item(item):
   print(f"Processing {item}")

with DAG(dag_id='dynamic_dag_with_for_loop',
        start_date=datetime(2025, 1, 1),
        schedule_interval=None,
        catchup=False) as dag:
   items = ["A", "B", "C"]
   for item in items:
       tasks = PythonOperator(
           task_id=f"process_{item}",
           python_callable=process_item,
           op_args={item},
       )
