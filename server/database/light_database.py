import motor.motor_asyncio
from bson.objectid import ObjectId #bson comes installed as a dependency of motor.
#from decouple import config


#MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable. if you delete comment "MONGO_DETAILS" You can use MongoDB atlas 
MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.testDB

light_collection = database.get_collection("vault001_collection")

# In the code above, we imported Motor, defined the connection details, and created a client via AsyncIOMotorClient.


# helpers
# create a quick helper function for parsing the results from a database query into a Python dict.

def light_helper(light) -> dict:
    return {
        "id": str(light["_id"]),
        "lightNumber": light["lightNumber"],
        "state": light["state"],
        "color": light["color"],
        "startTime": light["startTime"],
        "endTime": light["endTime"],
        "totalTime": light["totalTime"]
    }


# Retrieve all light bulb data present in the database

async def retrieve_lights():
    lights = []
    async for light in light_collection.find():
        lights.append(light_helper(light))
    return lights


# Retrieve a light with a maching ID

async def retrieve_light_data(id: str) -> dict:
    light = await light_collection.find_one({"_id", ObjectId(id)})
    if light:
        return light_helper(light)


# Add a new light bulb data into the database

async def add_light_bulb(light_data: dict) -> dict:
    light = await light_collection.insert_one(light_data)
    new_light = await light_collection.find_one({"_id": light.inserted_id})
    return light_helper(new_light)


# Update a light bulb with a maching ID

async def update_light(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
            return False
    light = await light_collection.find_one({"_id": ObjectId(id)})
    if light:
        updated_light = await light_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if updated_light:
        return True
    return False


# Delete a light bulb from the database

async def delete_light(id: str):
    light = await light_collection.find_one({"_id": ObjectId(id)})
    if light:
        await light_collection.delete_one({"_id": ObjectId(id)})
        return True