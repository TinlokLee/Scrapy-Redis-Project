import json
import redis
import MySQLdb

def main():

    # 指定 Redis 数据库信息
    rediscli = redis.StrictRedis(host='192.168.255.255', port=6379, db=0)

    # 指定 MySQL 数据库
    mysqlcli = MySQLdb.connect(host='127.0.0.1', user='Lee',passwd='666666',
                                db='youyuan', port=3306, use_unicode=True)
    while True:
        # FIFO 模式为 blpop，LIFO 模式为 brpop，获取键值
        source, data = rediscli.blpop(['youyuan:items'])
        item = json.loads(data)
        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            cur.execute("INSERT INTO beijing_18_25 (username, crawled, age, spider, header_url, source, pic_urls, monologue, source_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )", 
                        [item['username'], item['crawled'], item['age'], item['spider'], item['header_url'],
                        item['source'], item['pic_urls'], item['monologue'], item['source_url']]
                        )

            # 提交 sql 事务
            mysqlcli.commit()
            # 关闭本次操作
            cur.close()
            print('Inserted %s' % item['source_url'])
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


if __name__ == "__main__":
    main()