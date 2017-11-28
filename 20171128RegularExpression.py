# -*- coding: utf-8 -*-
import re
#re模块 转义r
# s1 = 'ABC\\-001'
# s2 =r'ABC\-001' 
# print(s1,s2)

#re.match()返回一个对象
# test = input()
# if re.match(r'正则表达式',test):
# 	print('匹配成功')
# else:
# 	print('匹配失败')

#切分字符串
# str = 'a b    c'
# print(str.split(' ')) # ['a', 'b', '', '', '', 'c']
# print(re.split(r'[\s]+',str))
# strs = 'a, b, c;; h'
# print(re.split(r'[\s\,\;]+',strs))


# #分组
# m = re.match(r'^(\d{3})-(\d{3,8})$','029-83145678')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# #贪婪匹配
# m = re.match(r'^(\d+)(0*)$','102300')
# print(m.group(0)) #'102300' ,' '

# n = re.match(r'^(\d+?)(0*)$','102300')
# print(n.group(1),n.group(2))

#编译
#预编译正则表达式
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# print(re_telephone.match('010-12345').groups())


#练习，验证email地址的正则表达式
# r = re.compile(r'([0-9a-zA-z_.]+)@([0-9a-zA-Z]+)\.(\w{3})')
# def is_valid_email(addr):
# 	if r.match(addr):
# 		print('is valid email')
# 	else:
# 		print('is not valid eamil')
# is_valid_email('someone@gmail.com')
# is_valid_email('bill.gates@microsoft.com')
# is_valid_email('bob#example.com')
# is_valid_email('mr-bob@example.com')
# print('ok')
