
#初始化累加变量
sum = 0
itr = 1

#计算从1到99的求和
while itr <= 100:
    #计算累加结果
    sum = sum + itr
    #更新累加数值
    itr = itr + 1

#求和乘以315再对21求余数
r = (sum * 315) % 21

#判断余数结果
if r >= 0 and r <= 6:
    print('haha')
elif r >= 7 and r <= 15:
    print('hehe')
elif r >= 16 and r <= 18:
    print('heihei')
else:
    print('xixi')