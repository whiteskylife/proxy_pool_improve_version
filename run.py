from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer)


def main():
    s = Scheduler()
    try:
        s.run()
        s.log().info('-------start process-------主进程开始运行...')
    except Exception as e:
        s.log().exception(e)
        main()


if __name__ == '__main__':
    main()
