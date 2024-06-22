import asyncio
import time

from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

class OrderRequest(BaseModel):
    item: str

@router.post("/hungry")
async def hungry(order: OrderRequest):
    item = order.item.lower()
    if item == "burgers":
        fries_task = asyncio.create_task(make_fries())
        await fries_task          
        burgers_task = await make_burgers()                  
    elif item == "fries":
        task = asyncio.create_task(make_fries())
    else:
        raise HTTPException(status_code=400, detail="Invalid item requested. Please specify 'burgers' or 'fries'.")
    
    # await task
    return f"{order.item.capitalize()} are ready!"

async def make_burgers():
    # simulating i/o bound stuff, then you want to use asyncio.sleep(time)
    print("Heating up stove top")    
    time.sleep(2)
    print("Throw burgs on stove")
    await asyncio.sleep(1)
    print("Burgers are ready!")

async def make_fries():
    print("Heating up fry oil")
    await asyncio.sleep(1)
    print("Put fries into oil")
    await asyncio.sleep(1)
    print("Fries are ready!")

app.include_router(router)