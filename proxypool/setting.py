# Redis数据库地址
REDIS_HOST = '192.168.1.110'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'redis-pass'

REDIS_KEY = 'proxies_2'

# 代理分数
# 初始分数设置为INITIAL_SCORE，检测代理是否有效：
# 如果：
#   通过就设置为MAX_SCORE；
#   不通过，此时代理分数大于MIN_SCORE，那么分数-1；否则，直接移除
MAX_SCORE = 10
MIN_SCORE = 8
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 10
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10

# Scheduler日志文件名：
LOG_PATH = 'schedule_getter.log'