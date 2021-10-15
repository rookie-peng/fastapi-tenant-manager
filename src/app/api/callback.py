import time
import logging
import requests


def callback(tenant, callback_body):
    time.sleep(3)
    # print("sleep 3s")
    response = requests.post(tenant['callback'], json=callback_body, timeout=10)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}
    # response = requests.post("http://127.0.0.1:9001", json=callback_body, headers=headers, timeout=10)
    logging.info(
        f'wait for 3s, callback  iam-service-management for {tenant["type"]} resource application, resp status: %s',
        response.status_code)



