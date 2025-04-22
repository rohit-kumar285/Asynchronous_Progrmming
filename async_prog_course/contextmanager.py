import asyncio
from contextlib import asynccontextmanager

## USING ASYNCCONTEXTMANAGER

# @asynccontextmanager
# async def connection():
#     print("Setting up connection")
#     await asyncio.sleep(1)
#     yield {"driver":"sqlite"}
#     await asyncio.sleep(1)
#     print("Connection Closed")


# async def main():
#     async with connection() as db : 
#         print(db,"is ready")

## USING MAGIC METHOD

class Connection:
    async def __aenter__(self):
        print("Setting up a Connection")
        await asyncio.sleep(2)
        return {"driver":"sqllite"}

    
    async def __aexit__(self,exc_type,exc,tb):
        await asyncio.sleep(1)
        print("Connection is closed")
        
async def main():
    async with Connection() as db:
        print(db,"is ready")


asyncio.run(main())


