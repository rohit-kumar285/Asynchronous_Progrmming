import asyncio

async def timer(name,seconds):
    while seconds:
        print(f"CountDown {name}: {seconds} seconds remaining")
        await asyncio.sleep(1)
        seconds = seconds-1
    print(f"CountDown {name} : Times's up !")


async def main():
    await asyncio.gather(timer('A',5),timer('B',4),timer('C',3))


asyncio.run(main())