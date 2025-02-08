from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
import os
from airflow.hooks.base import BaseHook
from airflow.models import Variable

def get_token():
    conn = BaseHook.get_connection("api_auth")
    url =  Variable.get("api_token_url")
    payload = {
        "username": conn.login,
        "password": conn.password
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")

def fetch_and_store_logistict():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = Variable.get("api_logistict_url")
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    now = datetime.now()
    date_path = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    output_dir = Variable.get("api_token_logistict_local_storage").format( date_path = date_path )
    os.makedirs(output_dir, exist_ok=True)

    filename = Variable.get("api_logistict_file").format( timestamp = timestamp )

    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 2, 8),
    "retries": 3,  # Número de tentativas
    "retry_delay": timedelta(minutes=1),  # Tempo entre tentativas
}

dag = DAG(
    "fetch_logistict",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

fetch_task = PythonOperator(
    task_id="fetch_and_store_logistict",
    python_callable=fetch_and_store_logistict,
    dag=dag,
)
