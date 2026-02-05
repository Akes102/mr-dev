import asyncio
import time

async def task(name):
    print(f"Starting task {name}")
    await asyncio.sleep(2)
    print(f"Finished task {name}")
    return f"Result of task {name}"

async def run_asyncio():
    results = await asyncio.gather(task("A"), task("B"), task("C"))
    return list(results)

if __name__ == "__main__":
    start_time = time.perf_counter()
    results = asyncio.run(run_asyncio())
    elapsed_time = time.perf_counter() - start_time

    print("Asyncio results")
    for result in results:
        print(f" {result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran concurrently using asyncio — modern approach for I/O-bound tasks")
