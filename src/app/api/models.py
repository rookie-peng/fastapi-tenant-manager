from pydantic import BaseModel, Field


class TenantSchema(BaseModel):
    callback: str = Field(..., min_length=10, max_length=200)
    tier: str = Field(..., min_length=1, max_length=50)
    type: str = Field(..., min_length=1, max_length=50)
    projectCode: str = Field(..., min_length=1, max_length=50)
    projectName: str = Field(..., min_length=1, max_length=50)


class TenantDB(TenantSchema):
    tenant_id: str = Field(..., min_length=1, max_length=50)


class User(BaseModel):
    userAccount: str = Field(..., min_length=1, max_length=50)
    userPasswd: str = Field(..., min_length=1, max_length=50)

