import uvicorn
from fastapi import FastAPI

from src.app.api import create_api, ping
from src.app.db import database, engine, metadata
# from app.api import create_api, ping
# from app.db import database, engine, metadata


# Create all tables stored in this metadata.
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(create_api.router, prefix="/devops-workorder", tags=["tenants"])


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=9000, reload=True, debug=True)