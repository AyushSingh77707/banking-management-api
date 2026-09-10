from pydantic import BaseModel,Field
from typing import Literal

class CustomerQueryParameter(BaseModel):
    page:int=Field(default=1,ge=1)
    limit:int=Field(default=10,ge=1,le=100)

    search:str | None=None

    status:Literal["ACTIVE","FROZEN","BLOCKED","INACTIVE"] | None=None

    sort_by:Literal["full_name","created_at"]="created_at"

    order:Literal["asc","desc"]="desc"

    @property
    def offset(self):
        return (self.page-1)*self.limit