import asyncio

async def cancel_corutine():
    count = 0
    while True:
        await asyncio.sleep(1)
        count+=1
        print(count)


async def main():
    task = asyncio.create_task(cancel_corutine())
    await asyncio.sleep(4)
    task.cancel()



asyncio.run(main())