import asyncio
import time 

def fetch(url):
    """Make a request, and fetch the results"""
    pass

def worker(name, queue, results):
    """Worker function to take unmade requests and execute requests then add results to results list"""
    pass

async def distribute_work(url, requests, concurrency, results):
    """Divide the work into matches and collect final results """
    queue = asyncio.Queue()

    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker - {i +1}", queue, results))
        tasks.append(task)
    
    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic - started_at

    for task in tasks:
        task.cancel()

    print("---")
    print(
        f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests"
    )

def assault(url, requests, concurrency):
    """ Entrypoint to making requests """
    results =[]
    asyncio.run(distribute_work(url, results, concurrency, results))
    print(results)
    