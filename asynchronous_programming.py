import asyncio 

async def say_hello():
    print("Hello")
    await asyncio.sleep(3)
    print("World")
# asyncio.run(say_hello())


## Runing multiple tasks together 

async def task(name,seconds):
    print(f"Task {name} is started")
    await asyncio.sleep(seconds)
    print(f"Task {name} is done after {seconds}")


async def main():
    await asyncio.gather(task("A",3),task("B",3),task("C",4),say_hello())

asyncio.run(main())