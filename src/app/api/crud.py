from src.app.api.models import TenantSchema
from src.app.db import tenants, database


async def post(payload: TenantSchema, pri_key: str):
    query = tenants.insert().values(tenant_id=pri_key, callback=payload.callback, tier=payload.tier, type=payload.type, project_code=payload.project_code, project_name=payload.project_name)
    return await database.execute(query=query)


async def get(id: int):
    query = tenants.select().where(id == tenants.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = tenants.select()
    return await database.fetch_all(query=query)


# async def put(id: int, payload: TenantSchema):
#     query = (
#         tenants
#         .update()
#         .where(id == tenants.c.id)
#         .values(title=payload.title, description=payload.description)
#         .returning(tenants.c.id)
#     )
#     return await database.execute(query=query)


async def delete(id: int):
    query = tenants.delete().where(id == tenants.c.id)
    return await database.execute(query=query)
