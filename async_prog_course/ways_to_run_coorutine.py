import asyncio


async def download():
    print('download function')

async def log():
    print('log function')

async def main():
    print('inside main functiion')

    # 2. using await keyword
    await download()

    # 3. using tasksl
    asyncio.create_task(log())


## 1. using asycio.run()
asyncio.run(main())