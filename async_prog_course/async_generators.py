import asyncio

async def downloads(urls):
    for url in urls:
        await asyncio.sleep(2)
        response = {"status":200,"data":f"Content of {url}"}
        yield response


async def main():
    urls = ["google.com","bing.com",'DuckDuckGo.com']
    async for url in downloads(urls):
        print(url)

asyncio.run(main())