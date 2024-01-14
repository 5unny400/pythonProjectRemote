import uuid
# uuid.uuid1([node[, clock_seq]])：基于主机ID和当前时间生成UUID。
# 如果给定了node参数（通常是硬件地址），则用它代替主机ID，如果给定了clock_seq参数，则用它代替随机序列。
uuid1 = uuid.uuid1()
print("uuid1:"+str(uuid1))

# uuid.uuid3(namespace, name)：基于MD5散列算法使用给定的namespace和name生成UUID。
namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
name = 'example_name'
uuid3 = uuid.uuid3(namespace, name)
print("uuid3:"+str(uuid3))

# uuid.uuid4()：基于随机数生成UUID。
uuid4 = uuid.uuid4()
print("uuid4:"+str(uuid4))

# uuid.uuid5(namespace, name)：基于SHA-1散列算法使用给定的namespace和name生成UUID。
namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
name = 'example_name'
uuid5 = uuid.uuid5(namespace, name)
print("uuid5:"+str(uuid5))

# uuid.NAMESPACE_*：uuid模块提供了几个预定义的命名空间，如
# NAMESPACE_DNS、NAMESPACE_URL等，可以用于uuid3和uuid5。
#
# 这些函数提供了不同的方式来生成UUID，具体选择取决于你的需求。通常，uuid4是生成随机UUID的常见选择。