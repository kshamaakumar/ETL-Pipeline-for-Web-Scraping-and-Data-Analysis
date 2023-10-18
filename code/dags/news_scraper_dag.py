from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.base_hook import BaseHook

# Define default_args for the DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 10, 17),
}

# Define the DAG
dag = DAG(
    'news_scraper_dag',
    default_args=default_args,
    description='Automated News Scraper DAG',
    schedule_interval=timedelta(days=1),
)

# Define tasks
start = DummyOperator(
    task_id='start',
    dag=dag,
)

# Define PythonOperator tasks for each step in your project
def scrape_data():
    # Use Python code from scrape_data.py
    exec(open("../scrape_data.py").read())

scrape_task = PythonOperator(
    task_id='web_scrape_task',
    python_callable=scrape_data,
    dag=dag,
)

def transform_data():
    exec(open("../data_transformation.ipynb").read())

transform_task = PythonOperator(
    task_id='data_transformation_task',
    python_callable=transform_data,
    dag=dag,
)

def visualize_data():
    exec(open("../data_viz.ipynb").read())

viz_task = PythonOperator(
    task_id='data_visualization_task',
    python_callable=visualize_data,
    dag=dag,
)

start >> scrape_task >> transform_task >> viz_task
