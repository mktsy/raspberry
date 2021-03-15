# This schema will help users send HTTP requests with the proper shape to the API -- e.g., the type of data to send and how to send it.
from typing import Optional
from pydantic import BaseModel, Field
import datetime
from typing import Optional


class LightSchema(BaseModel):
    lightNumber: int = Field(...)
    state: str = Field(...)
    color: str = Field(...)
    startTime: str = Field(...)
    endTime: str = Field(...)
    totalTime: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "lightNumber": 1,
                "state": "0",
                "color": "white",
                "startTime": datetime.datetime.now(),
                "endTime": "0",
                "totalTime": 0,
            }
        }


class UpdateLightModel(BaseModel):
    lightNumber: Optional[int]
    state: Optional[str]
    color: Optional[str]
    startTime: Optional[str]
    endTime: Optional[str]
    totalTime: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "lightNumber": 1,
                "state": "0",
                "color": "white",
                "startTime": datetime.datetime.now(),
                "endTime": "0",
                "totalTime": 0
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

# In the code above, we defined a Pydantic Schema called StudentSchema that represents how the student data will be stored in your MongoDB database.