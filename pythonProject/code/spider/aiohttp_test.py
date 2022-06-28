# -*-coding:utf-8-*-
import asyncio
import re

import aiohttp

TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.DOTALL)


async def get_web_title(url):
    async with aiohttp.ClientSession(headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }) as session:
        async with session.get(url, ssl=False) as resp:
            if resp.status == 200:
                html_info = await resp.text()
                title_info = TITLE_PATTERN.search(html_info)
                title = title_info.group(1).strip()
                print(f'{url} ==> {title}')


def main():
    urls = [
        'https://www.python.org/',
        'https://www.jd.com/',
        'https://www.baidu.com/',
        'https://www.taobao.com/',
        'https://www.iqiyi.com/',
        'https://www.sohu.com/',
        'https://gitee.com/',
        'https://www.amazon.com/',
        'https://www.tudou.com/',
        'https://www.nasa.gov/'
    ]
    result = [get_web_title(url) for url in urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(result))
    loop.close()


if __name__ == '__main__':
    main()
