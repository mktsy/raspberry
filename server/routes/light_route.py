# We'll be using the JSON Compatible Encoder from FastAPI to convert our models into a format that's JSON compatible.
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database.light_database import(
    retrieve_lights,
    retrieve_light_data,
    add_light_bulb,
    update_light,
    delete_light,
)
from server.model.light_schema import(
    LightSchema,
    UpdateLightModel,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()


@router.get("/", response_description="Light retrieved")
async def get_lights():
    lights = await retrieve_lights()
    if lights:
        return ResponseModel(lights, "lights data retrieved successfully")
    return ResponseModel(lights, "Empty list returned")


@router.get("/{id}", response_description="Light data retrieved")
async def get_light_data(id):
    light = await retrieve_light_data(id)
    if light:
        return ResponseModel(light, "Light data retrived successfully")
    return ErrorResponseModel("An error occurred.", 404, "Light doesn't exist.")


@router.post("/", response_description="Light data added into the database")
async def add_light_data(light: LightSchema = Body(...)):
    light = jsonable_encoder(light)
    new_light = await add_light_bulb(light)
    return ResponseModel(new_light, "Light added successfully")


@router.put("/{id}",)
async def update_light(id: str, req: UpdateLightModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_light = await update_light(id, req)
    if updated_light:
        return ResponseModel(
            "Light with ID: {} update is successful".format(id),
            "Light updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data"
    )


@router.delete("/{id}", response_description="Light data deleted from the data base")
async def delete_light_data(id: str):
    deleted_user = await delete_light(id)
    if deleted_user:
        return ResponseModel(
            "Light with ID: {} removed".format(id), "Light deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Light with id {0} doesn't exist".format(id)
    )