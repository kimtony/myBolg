import math
n = 10
width = 2*math.pi/n
x = []
for i in range(n):
  x.append(i*width) #获取所有等分点的横坐标
#用列表推导式来运算,所有将所有width放入列表x中
y = [abs(math.sin(i)) for i in x] #取所有横坐标正弦值的绝对值        
s = sum(y)*width
s
