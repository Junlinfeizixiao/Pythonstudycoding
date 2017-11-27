# -*- coding:utf-8 -*-

#weight = 80.5
#height = 1.75
#bmi = (weight/(height*height))
#print('%1.1f'%bmi)

#if bmi<18.5:
#	print('过轻')
#elif bmi<25:
#	print('正常')
#elif bmi<28:
#	print('过重')
#elif bmi<32:
#	print('肥胖')
#else:
#	print('严重肥胖')


#L = ['Bart','Lisa','Adam']
#for name in L:
#	print('Hello,%s'%name)
#i = 0
#while i<=2:
#	print('Hello,%s'%L[i])
#	i += 1

#n1 = 255
#n2 = 1000
#print(str(hex(n1)))
#print(str(hex(n2)))

# def trim(s):
# 	if s[:1] == " ":
# 		return trim(s[1:])
# 	elif s[-1:] == " ":
# 		return trim(s[:-1])
# 	else:
# 		return s
# str = "                                  jngjhghj"
# print(trim(str))

# def  findMinAndMax(*s):
# 	if s == None:
# 		return (None,None)
# 	else:
# 		max = s[0]
# 		min = s[0]
# 		for i in s:
# 			if i > max:
# 				max = i
# 			if i <= min:
# 				min = i
# 	return (max,min)

# s = [1,2,3,5,4,3]
# print(findMinAndMax(s))


#列表生成式
# L = [x * x for x in range(1,11)]
# print(L)
# L = [x * x for x in range(1,11)if x % 2 == 0]
# print(L)
# import os
# D = [d for d in os.listdir('.')]
# print(D)

# x = 'abc'
# y = 123
# print(isinstance(x,str)) #检查类型是否匹配
# print(isinstance(y,str))
# print(isinstance(y,int))

# L1 = ['Hello','World',18,'Apple',None]
# L2 = [x for x in L1 if (isinstance(x,str) == True) ]
# print(L2)

#高阶函数 map/reduce

# def f(x):
# 	return x*x

# r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

# s=list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(s)

# from functools import reduce #从外部调用reduce

# def add(x,y):
# 	return x+y

# result = reduce(add,[1,3,5,7,9]) #实现累加
# print(result)

# def fn(x,y):
# 	return x * 10 + y
# result = reduce(fn,[1,3,5,7,9])
# print(result)

# def normalize(name):
#     if isinstance(name, str) == True:
#         return name[0].upper() + name[1:].lower()
# L1 = ['adam','LISA','barT']
# L2 = list(map(normalize,L1))
# print(L2)

# from functools import reduce
# def prod(L):
# 	return reduce(lambda x,y:x*y,L) #匿名函数
# print('3 * 5 * 7 * 9 = ',prod([3,5,7,9]))
# if prod([3,5,7,9]) == 945:
# 	print('测试成功！')
# else:
# 	print('测试失败！')

# from functools import reduce

# def str2float(s):
# 	def fn(x,y):
# 		return x*10+y
# 	def char2float(s):
# 		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

# 	if '.' in s:
# 		i = s.index('.')
# 		s = s.replace('.','')
# 	x = reduce(fn,map(char2float,s))/(10 ** i)
# 	return x
# if abs(str2float('123.456')-123.456)<0.0001:
# 	print('测试成功！')
# else:
# 	print('测试失败！')

# def by_name(t):
# 	return t[0]
# def by_score(t):
# 	return t[1]

# L1 = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# L2 = sorted(L1,key=by_name)
# L3 = sorted(L1,key=by_score,reverse = True)
# print(L2)
# print(L3)

# L = list(filter(lambda x : x % 2 == 1,range(1,20)))
# print(L)


#面向对象
# class Student(object):
# 	pass
# bart = Student()
# bart

# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name,score):
# 		self.name = name   #公有成员，外界可以随意访问
# 		self.score = score
# 		#self.__name = name 私有成员__name
# 		#self.__score = score 公有成员 __score
# 	def print_score(std):
# 		print("%s:%s"%(std.name,std.score))
# 	def get_grade(self):
# 		if self.score >= 90:
# 			print('A')
# 		elif self.score >= 60:
# 			print('B')
# 		else:
# 			print('C')
# bart = Student('xiao ming',79)
# bart.print_score()
# bart.get_grade()

# -*- coding:utf-8 -*-
# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self,name,gender) :
# 		self.name = name
# 		self.__gender = gender
# 	def get_gender(self):
# 		return self.__gender
# 	def set_gender(self,g):
# 		self.__gender = g
		
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

#继承，多态，检查类型

# class Animal(object):
# 	def run(self):
# 		print('animal is running')
# class Dog(Animal):
# 	def run(self):
# 		print('Dog is running')
# class Cat(Animal):
# 	def run(self):
# 		print('Cat is running')

# def runonce(ani):
# 	ani.run()
	
# animal = Animal()
# dog = Dog()
# cat = Cat()
# animal.run()
# cat.run()
# dog.run()
# runonce(animal)
# runonce(dog)
# runonce(cat)


#读写文件
with open('path','r') as f:
	print(f.read()) #一次读完所有文件	
for line in f.readlines() #一次读一行并删掉末尾的'\n'
	print(line.strip())
#读二级制文件 'rb',错误忽略
with open('path','r',encoding = 'gbk',errors = 'ignore') as f:
	pass
#写文件，要编入特定的编码:encoding = '...'
with open('path','w') as f:
	f.write('hello,world')
