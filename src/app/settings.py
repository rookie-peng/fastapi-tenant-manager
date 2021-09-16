import os


# def get_env_value(env_var, default=''):
#     """Try to get a env_variable, this handles the KeyError Exception"""
#     try:
#         return os.environ[env_var]
#     except Exception:
#         if default != '':
#             return default
#         error_msg = f'Missing **required** environment variable {env_var}'
#         raise ImproperlyConfigured(error_msg)


TENANT_SHARED_RESOURCE_REDIS_URL = '10.72.2.17:6379'
TENANT_SHARED_RESOURCE_REDIS_KEY = 'foobared'
TENANT_SHARED_RESOURCE_MONGO = 'rcdbaer:rc-manger123@10.72.2.17:27020,10.72.2.17:27021,10.72.2.17:27022'
TENANT_SHARED_RESOURCE_INFLUX = '10.72.2.17:8086'
TENANT_SHARED_RESOURCE_HIVE = '10.72.2.17:10000 10.72.2.17:8080'
TENANT_SHARED_RESOURCE_KAFKA = '10.72.2.17:9092'
TENANT_SHARED_RESOURCE_FLINK = '10.72.2.17:8081'
TENANT_SHARED_RESOURCE_EMQ = '10.72.2.17:1883'