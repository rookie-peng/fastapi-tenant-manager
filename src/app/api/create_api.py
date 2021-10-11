import logging
import requests
from typing import List
from fastapi import APIRouter, HTTPException, Path

# from src.app.api import crud
# from src.app import settings
# from src.app.api.models import TenantDB, TenantSchema
from app.api import crud
from app import settings
from app.api.models import TenantDB, TenantSchema

router = APIRouter()
logging.getLogger().setLevel("INFO")


@router.post("/", response_model=TenantDB, status_code=201)
async def create_note(payload: TenantSchema):
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


# @router.post("/api/tenantResourceApply/tenants/{tenantId}/services", response_model=TenantDB)
@router.post("/api/tenantResourceApply/tenants/{tenantId}/services")
async def create_order(request: TenantSchema, tenantId: str):
    body = request
    pri_key = tenantId
    res = vars(body)
    res["tenant_id"] = tenantId
    logging.info('tenant content: %s', res)
    await crud.post(body, pri_key)

    try:
        resource = await on_resource_apply(res)

    except Exception as e:
        print(str(e))
    return resource


async def on_resource_apply(tenant):
    """
    Entry point for resource application
    """
    resource = "type error!"
    if tenant["type"] == 'cms':
        resource = await on_cms_apply(tenant)
        pass
    elif tenant["type"] == 'otds':
        resource = await on_otds_apply(tenant)
        pass
    else:
        logging.warn('Unsupported Resource Type: %s', tenant["type"])
    return resource


async def on_cms_apply(tenant):
    """
    handle cms resource application
    """
    resp = {}
    resp['tenant'] = tenant
    # 假设全部成功
    resp['code'] = 0
    resp['msg'] = '创建成功'
    resp['flag'] = True

    tier = tenant['tier']

    shared_redis_url = settings.TENANT_SHARED_RESOURCE_REDIS_URL
    shared_redis_key = settings.TENANT_SHARED_RESOURCE_REDIS_KEY
    shared_mongo = settings.TENANT_SHARED_RESOURCE_MONGO
    shared_influx = settings.TENANT_SHARED_RESOURCE_INFLUX
    shared_hive = settings.TENANT_SHARED_RESOURCE_HIVE
    shared_kafka = settings.TENANT_SHARED_RESOURCE_KAFKA
    shared_flink = settings.TENANT_SHARED_RESOURCE_FLINK
    shared_emq = settings.TENANT_SHARED_RESOURCE_EMQ

    resources = [{
        "mode": "single",
        "eachNodeCores": 0,
        "nodeNum": 3,
        "eachNodeMemory": 6,
        "eachNodeDisk": 0,
        "accessKey": shared_redis_key,
        "accessUrl": shared_redis_url,
        "resourceLevel": tier,
        "type": "redis",
        "version": "4"
    }, {
        "mode": "replica",
        "eachNodeCores": 12,
        "nodeNum": 3,
        "eachNodeMemory": 32,
        "eachNodeDisk": 500,
        "resourceLevel": tier,
        "type": "mongo",
        "version": "4",
        "accessUrl": shared_mongo
    }, {
        "eachNodeCores": 2,
        "nodeNum": 12,
        "eachNodeMemory": 3,
        "eachNodeDisk": 2000,
        "resourceLevel": tier,
        "type": "influx",
        "version": "1.8",
        "accessUrl": shared_influx
    }, {
        "resourceLevel": tier,
        "queryHiveUrl": shared_hive,
        "type": "hive",
        "hiveUrl": shared_hive,
        "version": "3.1.0"
    }, {
        "kafkaBroadcastAddress": shared_kafka,
        "resourceLevel": tier,
        "type": "kafka",
        "version": "2.3.0"
    }, {
        "resourceLevel": tier,
        "type": "flink",
        "flinkJobManageAddress": shared_flink,
        "version": "1.9.3"
    }, {
        "resourceLevel": tier,
        "type": "emq",
        "version": "3.2.6",
        "emqServerUrl": shared_emq,
    }]

    resp['data'] = resources
    response = requests.post(tenant['callback'], json=resp, timeout=10)
    logging.info(
        'call iam-service-management for CMS resource application, resp status: %s',
        response.status_code)
    return resp


async def on_otds_apply(tenant):
    """
    handle otds resource application
    """
    resp = {}
    resp['tenant'] = tenant
    # 假设全部成功
    resp['code'] = 0
    resp['msg'] = '创建成功'
    resp['flag'] = True
    tier = tenant['tier']

    shared_mongo = settings.TENANT_SHARED_RESOURCE_MONGO
    shared_influx = settings.TENANT_SHARED_RESOURCE_INFLUX
    shared_hive = settings.TENANT_SHARED_RESOURCE_HIVE
    shared_redis_url = settings.TENANT_SHARED_RESOURCE_REDIS_URL
    shared_redis_key = settings.TENANT_SHARED_RESOURCE_REDIS_KEY

    resources = [{
        "mode": "replica",
        "eachNodeCores": 12,
        "nodeNum": 3,
        "eachNodeMemory": 32,
        "eachNodeDisk": 200,
        "resourceLevel": tier,
        "type": "mongo",
        "version": "4",
        "accessUrl": shared_mongo
    }, {
        "eachNodeCores": 2,
        "nodeNum": 12,
        "eachNodeMemory": 4,
        "eachNodeDisk": 300,
        "resourceLevel": tier,
        "type": "influx",
        "version": "1.8",
        "accessUrl": shared_influx,
    }, {
        "resourceLevel": tier,
        "queryHiveUrl": shared_hive,
        "type": "hive",
        "hiveUrl": shared_hive,
        "version": "3.1.0"
    }, {

        "mode": "cluster",
        "eachNodeCores": 0,
        "nodeNum": 3,
        "eachNodeMemory": 6,
        "eachNodeDisk": 0,
        "resourceLevel": tier,
        "type": "redis",
        "version": "4",
        "accessUrl": shared_redis_url,
        "accessKey": shared_redis_key,
    }]
    resp['data'] = resources
    print(resp)

    response = requests.post(tenant['callback'], json=resp, timeout=10)
    logging.info(
        'call iam-service-management for OTDS resource application, resp status: %s',
        response.status_code)
    return resp

