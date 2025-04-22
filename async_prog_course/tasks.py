import asyncio

async def Stopwatch():
    count =1
    while count<4:
        await asyncio.sleep(1)
        count+=1
        print(count)

def Callback(task):
    print("task is done :)",task)

async def main():
    print(asyncio.get_running_loop())
    task = asyncio.create_task(Stopwatch())
    # print(task)
    # print(task.get_coro())
    # print(task.get_name)
    task.add_done_callback(Callback)
    await task

asyncio.run(main())