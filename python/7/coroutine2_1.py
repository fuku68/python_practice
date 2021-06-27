import asyncio
import time

async def heavy_process(name, sec):
    print(f'start {name}')
    # ダミーの重い処理（sec秒だけ処理を休止）
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'

start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    heavy_process('Hoge', 5)
)
end = time.time()
print(result)
print(f'Process Time: {end - start}')
