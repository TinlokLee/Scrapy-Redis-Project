# 指定scrapy-redis 的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 指定scrapy-redis 的去重
DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy 默认)，由sorted set 实现的⼀种⾮FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# 可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# 可选的 按后进先出排序(LIFO)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack' 

# 在 redis 中保持 scrapy-redis用到的各个队列，从允许暂停和暂停后恢复，
# 也就是不清理 redis queues
SCHEDULER_PERSIST = True

# 只在使用SpiderQueue 或者 SpiderStack 是有效的参数，
# 指定爬虫关闭的最小间隔时间
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 这个已经由 scrapy-redis 实现，不需要我们写代码
ITEM_PIPELINES = {
'example.pipelines.ExamplePipeline': 300,
'scrapy_redis.pipelines.RedisPipeline': 400
}

# 指定 redis 数据库的连接参数
# REDIS_PASS 是我⾃⼰加上的 redis 连接密码，需要简单修改
#  scrapy-redis 的源代码以⽀持使⽤密码连接 redis（默认不做）
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
#REDIS_PASS = 'redisP@ssw0rd'

# LOG 等级
LOG_LEVEL = 'DEBUG'

#默认情况下,RFPDupeFilter 只记录第⼀个重复请求。
# 将 DUPEFILTER_DEBUG 设置为 True 会记录所有重复的请求。
DUPEFILTER_DEBUG =True


# 覆盖默认请求头，可以自己编写 Downloader Middlewares 设置代理和 UserAge
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, sdch'
}

