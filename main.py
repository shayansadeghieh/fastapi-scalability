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
    # asyncio.run(make_meal())
    if item == "burgers":                
        # burgers_task = await make_burgers()    
        b_task = make_burgers()
        # await b_task
        fries_task = asyncio.create_task(make_fries())                
        await fries_task  
        # await burgers_task

              
    # # elif item == "fries":
    # #     task = asyncio.create_task(make_fries())
    else:
        raise HTTPException(status_code=400, detail="Invalid item requested. Please specify 'burgers' or 'fries'.")
    
    # await task
    return f"{order.item.capitalize()} are ready!"
    

async def make_burgers():
    
    # simulating i/o bound stuff, then you want to use asyncio.sleep(time)
    print("Heating up stove top")        
    await asyncio.sleep(5)
    
    # time.sleep(2)
    print("Throw burgs on stove")
    await asyncio.sleep(1)
    print("Burgers are ready!")

async def make_fries():
    print("Heating up fry oil")
    await asyncio.sleep(1)
    print("Put fries into oil")
    await asyncio.sleep(1)
    print("Fries are ready!")

# async def make_meal():    
#     b_task = asyncio.create_task(make_burgers())
#     f_task = asyncio.create_task(make_fries())
#     await b_task
#     await f_task
#     return 

app.include_router(router)

"""
NOTES
- Order matters. If I do:
        await make_burgers()
        fries_task = asyncio.create_task(make_fries())                
        await fries_task  
    Then there will be no other tasks to run and await make_burgers() will block the fries_task from being created. 

- When to use tasks vs just coroutines
    If I do:
        await make_burgers()
        await make_fries()
    The make_burgers() coroutine will block make_fries() coroutine, until it is finished. 

    Instead, if I do:
        asyncio.create_task(make_burgers())
        asyncio.create_task(make_fries())
    This will kick off both coroutines "simultaneously". I then need to add an await for both tasks, as 
    this may result in the program exiting prior to the tasks completing. 

- Using a sync endpoint:
    If I do:
        @router.post("/hungry")
        def hungry(order: OrderRequest):  
            pass        
    Every request will spawn a new thread. fastAPI can handle a max of 40 threads. 

- Using an async endpoint:
    If I do:
        @router.post("/hungry")
        async def hungry(order: OrderRequest):  
            pass
    Uvicorn will create an event loop on a single thread. If there is anything blocking within that event loop, 
    we will effectively block all tasks and each request will basically complete sequentially. 
"""