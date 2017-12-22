'''
print("this i smy first program for python")

a = 21
b = 20
c = 0

if(a == b):
	print("a等于b")
else:
	print("a 不等于b")
	print("我早就知道啦")
'''
'''
a = 20
b = 20 

if(a == b):
	print("a 和 b 有相同的标识")
else:
	print("a 和 b 有不同的标识")

b = 30
if(a == b):
	print("a 和 b 有相同的标识")
else:
	print("a 和 b 有不同的标识")
'''
'''
c = 0b11111111
d = 0b0
print(c)
print(d)
print(c&d)
print(c|d)
print(bin(c))
print(bin(d))
print(oct(c))
print(oct(d))
print(hex(c))
print(hex(d))
'''
'''
a, b = 0, 1
while b < 1000:
	print(b, end = ",")
	a, b = b, a + b
'''

'''
print("请输入一个数字")
var = input()
if var:
	print("1-if表达式的条件为 true")
	print(var)

var = 0
if var:
	print("2-if条件表达式为 true")
	print(var)
print("goodbay")
'''
'''
while 1:
	age = int(input("请输入你家狗狗的年龄"))

	if age < 0:
		print("你说在逗我吧")
	elif age == 1:
		print("相当于一个14岁的人")
	elif age == 2:
		print("相当于22岁的人")
	elif age > 2:
		human = 22 + (age -2) * 5
		print("对应人类的年龄：",human)

	#退出提示
	input("点击enter继续")
'''

import sys

def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if counter > n:
			return
		yield a
		a, b = b, a + b
		counter += 1

f = fibonacci(10)

while True:
	try:
		print(next(f), end = " ")
	except StopIteration:
		sys.exit()






























