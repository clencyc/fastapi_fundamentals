from pedantic import BaseModel, conint, constr, confloat, conlist, field_validator
from typing import Optional
import re
class StudentBase(BaseModel):
    # id: int
    first_name: str
    last_name: str
    email: str
    
    
@field_validator('first_name')
@classmethod
def validate_last_name(cls, value):
    if len(value) < 3:
        raise ValueError('First name must be at least 3 characters long')
    if re.match(r"\s", value):
        raise valueError("Name must not contain spaces")
    return value



class StudentUpdate(BaseModel):
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    email : Optional[str] = None
    
    