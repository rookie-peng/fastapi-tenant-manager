import time
import logging
import requests


def callback(tenant, callback_body):
    time.sleep(3)
    # print("sleep 3s")
    response = requests.post(tenant['callback'], data=callback_body, timeout=10)
    logging.info(
        'wait for 3s, callback  iam-service-management for CMS resource application, resp status: %s',
        response.status_code)



