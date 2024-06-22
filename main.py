import asyncio 
import time

from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

# An app that makes burgers and fries 
@router.post("/hungry")
async def hungry():
    task_1 = asyncio.create_task(make_burgers())
    task_2 = asyncio.create_task(make_fries())
    await task_1
    await task_2
    return "Order is ready"

async def make_burgers():
    # simulatiing i/o bound stuff, then you want to use asyncio.sleep(time)
    print("Heating up stove top")
    await asyncio.sleep(2)
    print("Throw burgs on stove")
    await asyncio.sleep(1)
    print("Burgers are ready!")


async def make_fries():
    print("Heating up oil")
    await asyncio.sleep(1)
    print("Put fries into oil")
    await asyncio.sleep(1)
    print("Fries are ready!")

app.include_router(router)
