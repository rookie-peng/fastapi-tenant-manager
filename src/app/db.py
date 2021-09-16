import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL: str = 'mysql://root:123456@192.168.79.131:3306/tenant-management'

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
tenants = Table(
    "tenants",
    metadata,
    Column("tenant_id", String(50), primary_key=True),
    Column("callback", String(100)),
    Column("tier", String(50)),
    Column("type", String(50)),
    Column("project_code", String(50)),
    Column("project_name", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
