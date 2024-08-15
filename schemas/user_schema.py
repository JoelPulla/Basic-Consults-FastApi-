from pydantic import BaseModel
from typing import Optional, List

####### Esquema or Model ###
class User(BaseModel):
    id: Optional[int] = None
    name:str
    laste_name: str
    mail : str
    direcction : str
    number : str
    is_actie : bool

