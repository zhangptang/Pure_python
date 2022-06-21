# -*-coding:utf-8-*-
"""
异步io  async-await
"""
import asyncio
import math


def num_generator(m, n):
    yield range(m, n + 1)


async def prime_filter(m, n):
    primes = []
    for i in num_generator(m, n):
        flag = True
        num = int(math.sqrt(i))
        for j in range(2, num + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    squares = []
    for i in num_generator(m, n):
        print('square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)

    return squares


def main():
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()
