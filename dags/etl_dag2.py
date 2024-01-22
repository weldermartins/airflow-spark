import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id="welderteste2",
    default_args={
        "owner": "welder",
        "start_date": airflow.utils.dates.days_ago(1)
    },
    schedule_interval="@daily"
)

python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark-conn",
    application="jobs/python/transformation.py",
    dag=dag
)
python_job