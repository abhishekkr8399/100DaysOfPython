#|----------------------------------------------------------------|
#|Description    :    AsyncIO Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import time
import asyncio
async def function1():
    await asyncio.sleep(1)
    # time.sleep(1)
    print("function-1")
async def function2():
    await asyncio.sleep(1)
    # time.sleep(3)
    print("function-2")
async def function3():
    await asyncio.sleep(4)
    # time.sleep(3)
    print("function-3")

async def main():
    L=await asyncio.gather(function1(),function2(),function3(),)
    print(L)
    # task=asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

asyncio.run(main())