import sys
sys.path.append("SparkingFlow")
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

from os.path import join
from airflow.utils.dates import days_ago
from pathlib import Path


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 1, 22),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(dag_id = "TwitterDAG", default_args=default_args,
         start_date=days_ago(6), schedule_interval="@daily") as dag:

    twitter_transform = SparkSubmitOperator(task_id="transform_twitter_datascience",
                                            conn_id="spark-conn",
                                            application="jobs/python/transformation.py",
                                            name="twitter_transformation")



    twitter_transform