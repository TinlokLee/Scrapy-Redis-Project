import json
import redis
import pymongo

def main():

    # 指定 Redis 数据库信息
    rediscli = redis.StrictRedis(host='192.168.255.255', port=6379, db=0)

    # 指定 MongoDB 数据库信息
    mongocli = pymongo.MongoClient(host='localhost', port=27017)

    # 创建数据库名
    db = mongocli['youyuan']

    # 创建表名
    sheet = db['beijingGirl']

    while True:
        # FIFO 模式为 blpop, LIFO 模式为 brpop, 获取键值
        source, data = rediscli.blpop(["youyuan:items"])
        item = json.loads(data)
        sheet.insert(item)

        try:
            print(u'Processing: %(name)s <%(link)s>' % item)
        except KeyError:
            print(u'Error processing: %r' % item)

if __name__ == "__main__":
    main()
    


