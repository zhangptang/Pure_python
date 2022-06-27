# -*-coding:utf-8-*-
import ssl

import builtwith
import whois
"""
爬虫基本流程
1.设定抓取目标（种子页面/起始页面）并获取网页。
2.当服务器无法访问时，按照指定的重试次数尝试重新下载页面。
3.在需要的时候设置用户代理或隐藏真实IP，否则可能无法访问页面。
4.对获取的页面进行必要的解码操作然后抓取出需要的信息。
5.在获取的页面中通过某种方式（如正则表达式）抽取出页面中的链接信息。
6.对链接进行进一步的处理（获取页面并重复上面的动作）。
7.将有用的信息进行持久化以备后续的处理。
"""



def builtwith_test():
    """
    builtwith --识别网站所用技术的工具
    :return:
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    print(builtwith.parse('http://www.bootcss.com/'))


def whois_test():
    """
    python-whois --- 查询网站所有者的工具
    :return:
    """
    print(whois.whois('https://www.bootcss.com'))


def main():
    builtwith_test()
    whois_test()


if __name__ == '__main__':
    main()
