#(©)CodeXBotz



import asyncio
import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]
admin_data = database['admins']
user_data = database['users']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

# Function to check if an admin exists
async def present_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    found = await loop.run_in_executor(None, lambda: admin_data.find_one({'_id': admin_id}))
    return bool(found)

# Function to add a new admin
async def add_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: admin_data.insert_one({'_id': admin_id}))
    return

# Function to retrieve all admins
async def full_adminbase():
    loop = asyncio.get_running_loop()
    admin_docs = await loop.run_in_executor(None, lambda: admin_data.find())
    admin_ids = []
    for doc in admin_docs:
        admin_ids.append(doc['_id'])
    return admin_ids

# Function to delete an admin
async def del_admin(admin_id: int):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: admin_data.delete_one({'_id': admin_id}))
    return
    
