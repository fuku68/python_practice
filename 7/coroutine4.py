import asyncio
import requests
import time

# 指定のURLにリクエストし、結果を取得
async def get_content(url):
    print(f'start {url}')
    res = requests.request('get', url)
    print(f'end {url}')
    return res.text[:100]

start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    asyncio.gather(
        get_content('https://codezine.jp'),
        get_content('https://wings.msn.to'),
        get_content('https://www.web-deli.com/')
    )
)

end = time.time()
print(result)
print(f'Process Time: {end - start}')
