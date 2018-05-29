import time
from multiprocessing import Process
from proxypool.api import app
from proxypool.getter import Getter
from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.setting import *
import logging
import os


class Scheduler():
    def log(self):
        if not os.path.exists('log'):
            os.mkdir('log')
        log_file_name = 'log/' + LOG_PATH
        log_file_1 = logging.FileHandler(log_file_name, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)s :  %(message)s")
        log_file_1.setFormatter(fmt)
        logger1 = logging.Logger('run_log', level=logging.INFO)
        logger1.addHandler(log_file_1)

        return logger1

    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        try:
            getter = Getter()
            while True:
                print('开始抓取代理')
                getter.run()
                time.sleep(cycle)
        except Exception as e:
            self.log().exception(e)

    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')

        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
