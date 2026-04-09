#Concurrent = multiple tasks are in progress at the same time but they are not necessarily running at the exact same instant
#Concurrency = taking turns
#Parallelism = running at the same exact time

import asyncio

async def task(name):
    print(f"Start {name}")
    await asyncio.sleep(5)
    print(f"End {name}")

async def main():
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())