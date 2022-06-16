# -*-coding:utf-8-*-
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class Account:
    """账户"""

    def __init__(self, balance=0):
        self._balance = balance
        _lock = threading.RLock()
        self._condition = threading.Condition(_lock)

    def deposit(self, money):
        """存钱"""
        with self._condition:
            new_balance = self._balance + money
            time.sleep(0.001)
            self._balance = new_balance
            self._condition.notify_all()

    def withdraw(self, money):
        """取钱"""
        with self._condition:
            while self._balance < money:
                self._condition.wait()
            new_balance = self._balance - money
            time.sleep(0.001)
            self._balance = new_balance

    @property
    def balance(self):
        return self._balance


def add_money(account):
    """存钱方法"""
    while account.balance < 100:
        money = random.randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '存入====>', account.balance)
        time.sleep(0.5)


def sub_money(account):
    while True:
        money = random.randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '取出<====', account.balance)
        time.sleep(1)


def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(10):
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()
