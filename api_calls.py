import asyncio
import aiohttp

async def fetch(session,url):
    print(f"Fetching url : {url}")
    async with session.get(url) as response:
        data = response.text
        print(f"Done with {url}")
        return data 
    
async def main():
    urls = [
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session,url) for url in urls]
        responses = await asyncio.gather(*tasks)


    print("All Done :)")
    print("=========================================")
    print(responses)
asyncio.run(main())