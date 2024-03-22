from Sophia import DATABASE
import asyncio
import random

db = DATABASE["IGNORE_BAD"]

class IGNORE_BAD:
    async def ENABLE(self):
        try:
            await db.update_one({"_id": 1}, {"$addToSet": {"IGNORE_BAD": True}})
            return "SUCCESS"
        except Exception as e:
            print("Error while enabling IGNORE_BAD", e)
            return e
    async def GET(self):
        Find = await db.find_one({"_id": 1})
        if not Find:
            return False 
        else:
            value = Find.get("IGNORE_BAD", False)
            return value
    async def DISABLE(self):
        try:
            await db.update_one({"_id": 1}, {"$set": {"IGNORE_BAD": False}})
            return "SUCCESS"
        except Exception as e:
            return e

