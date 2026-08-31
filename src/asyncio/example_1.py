import asyncio

import time

async def asyn_function_1():
    print("asynchronous_1 function started")
    time.sleep(2)
    print("asynchronous_1 function finished")

#this is a courotine
async def async_function():
    print("async function started")
    await asyncio.sleep(2)
    print("async function finished")

asyncio.run(async_function())