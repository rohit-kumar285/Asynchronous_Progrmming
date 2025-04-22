import asyncio 


async def say_hello():
    print("Hello dude :) ")
    await asyncio.sleep(2)
    print("Task Ended")

async def main():
    task = asyncio.create_task(say_hello())
    print("Doing other Tasks while it's runing !")
    await asyncio.sleep(2)
    print("we are still runing")
    await task

asyncio.run(main())