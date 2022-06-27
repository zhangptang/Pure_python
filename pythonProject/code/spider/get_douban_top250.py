# -*-coding:utf-8-*-
import random
import re
import time

import requests


def get_douban_top250(page):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
        proxies={
            'http': 'http://114.67.104.36:18888'
        }
    )
    pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
    titles = pattern1.findall(resp.text)
    pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span')
    ranks = pattern2.findall(resp.text)
    print(f'第{page}页数据如下：')
    for title, rank in zip(titles, ranks):
        print(f'book name: {title} ===> rank: {rank}')
    print('---------------')
    time.sleep(random.random() * 4 + 1)


def main():
    for page in range(1, 11):
        get_douban_top250(page)


if __name__ == '__main__':
    main()
