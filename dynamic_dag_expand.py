from airflow.decorators import task, dag
from datetime import datetime
@task
def process_item(item):
   print(f"Processing {item}")
@dag(schedule_interval=None, start_date=datetime(2025, 1, 1), catchup=False)
def dynamic_dag_with_expand():
   items = ["A", "B", "C"]
   process_item.expand(item=items)
dynamic_dag_with_expand()
