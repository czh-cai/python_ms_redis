# 1.导入模块
#import redis
from redis import Redis


# 2.实例化产生链接对象
# 连接本地的redis
conn = Redis(host='192.168.0.231', port=6379, db=0, password='123456')

# 3.获取redis数据库中键对应的值
ret = conn.hmget('BUS_HS',['store'],)
print(ret)

result = str(ret.__getitem__(0))
print(result)
