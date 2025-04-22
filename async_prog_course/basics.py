import asyncio

# async def main():
#     print("helo...")
#     await asyncio.sleep(4)
#     print("...world")

# asyncio.run(main())


## Asynchronous Iterators

class EggBoiler:
    def __init__(self,amount):
        self.eggs = iter(range(1,amount+1))

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        try:
            egg = next(self.eggs)
        except StopIteration:
            raise StopAsyncIteration
        return self.boil(egg)
    
    async def boil(self,egg):
        await asyncio.sleep(1)
        print(f"Egg #{egg} is boiling ")
        
async def main():
    eggs = []
    async for egg in EggBoiler(4):
        eggs.append(egg)
    
    await asyncio.gather(*eggs)
    print("We wait for the egg to boil ")

asyncio.run(main())