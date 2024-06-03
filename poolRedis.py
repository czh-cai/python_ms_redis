# 1.导入模块
import redis

# 2.建一个连接池
# max_connections指定池子里最多建100个连接
# decode_responses=True将二进制转换成字符串存储；decode_responses=False就是二进制储存
pool = redis.ConnectionPool(max_connections=100, host='192.168.0.231', port=6379, db=0, password='123456', decode_responses=True,)  # 这里还是一个不填host和port表示默认连接本地redis

# 3.这句话表示：从池子中拿出一个连接
r = redis.Redis(connection_pool=pool)

# ret = r.get('BUS_HS')
ret = r.hmget('BUS_HS',['store'])
print(ret.__getitem__(0))


