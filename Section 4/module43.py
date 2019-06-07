# Native concurrency with asyncio-
# [NOTE - Run this python script through Terminal, sometimes compiler makes issue]

# Importing asyncio (concurrency library in python)
import asyncio
# Importing time for time delay
import time



async def myTask():
    time.sleep(3) # to hold for 3 seconds
    print("Processing Task")

async def myTaskGenerator():
    for i in range(5):
        asyncio.ensure_future(myTask())
        print(asyncio.Task.all_tasks()) # For list of pending tasks


# initiated loop-
initiate_loop = asyncio.get_event_loop()

# running the task until it gets over-
initiate_loop.run_until_complete(myTaskGenerator())

# Signal to check if all tasks are completed
print("Completed All Tasks")

# Safely Closing loop
initiate_loop.close()

