import asyncio 
import inspect
import warnings
warnings.filterwarnings('ignore')

async def main():
    pass

print(type(main))

print(inspect.iscoroutinefunction(main))
print(type(main()))
print(dir(main()))