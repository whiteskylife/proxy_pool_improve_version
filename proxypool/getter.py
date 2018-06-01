from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.crawler import Crawler
from proxypool.setting import *
import sys
import os
import logging

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def log(self):
        if not os.path.exists('log2'):
            os.mkdir('log2')
        log_file_name = 'log2/' + LOG_PATH
        log_file_1 = logging.FileHandler(log_file_name, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        log_file_1.setFormatter(fmt)
        logger1 = logging.Logger('run_log', level=logging.DEBUG)
        logger1.addHandler(log_file_1)

        return logger1

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        """爬取到代理设置初始分数，直接存入redis"""
        print('获取器开始执行')
        if not self.is_over_threshold():
            try:
                for callback_label in range(self.crawler.__CrawlFuncCount__):
                    callback = self.crawler.__CrawlFunc__[callback_label]
                    # 获取代理
                    proxies = self.crawler.get_proxies(callback)
                    sys.stdout.flush()
                    if not proxies:
                        self.log().error('代理抓取失败，抓取函数：%s' % callback)
                        continue
                    for proxy in proxies:
                        self.redis.add(proxy)
            except Exception as e:
                self.log().exception(e)
