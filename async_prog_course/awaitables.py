## currently there are three awaitables in python 
## 1. coroutines
## 2. task
## 3. futures 

## however you can also create custom awaitables as shown 
import asyncio

class Stopwatch : 
    def __await__(self):
        yield 


async def main():
    await Stopwatch()

asyncio.run(main())