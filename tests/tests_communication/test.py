import asyncio

async def produce(queue, name):
    for i in range(5):
        await asyncio.sleep(1)
        item = f'{name}-{i}'
        await queue.put(item)
        print(f'{name} produced {item}')
    await queue.put(None)  # Signal completion

async def consume(queue, name):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'{name} consumed {item}')
        await asyncio.sleep(1)  # Simulate processing

async def main():
    queue = asyncio.Queue()

    producers = [produce(queue, 'Producer1'), produce(queue, 'Producer2')]
    consumers = [consume(queue, 'Consumer1'), consume(queue, 'Consumer2')]

    await asyncio.gather(*producers)
    await queue.join()  # Wait until the consumers have consumed all items
    for consumer in consumers:
        await queue.put(None)  # Signal consumers to stop
    await asyncio.gather(*consumers)

asyncio.run(main())