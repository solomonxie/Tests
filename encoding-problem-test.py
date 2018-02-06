#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 正常编码方式
# cn = '你好'
# ss = cn.decode('utf-8')
# print repr(ss)
# print ss.encode('utf-8')
# with open('test.txt', 'wt') as f:
#     f.write(ss.encode('utf-8'))
# with open('test.txt', 'r') as f:
# 	print( f.read() )



# 全部编码成url格式 如果不是获取外来文件的话是可以的 
# 但是打开文件或网络内容 就不行
# from urllib import quote
# from urllib import unquote
# cn = '你好'
# print cn
# ss = quote(cn)
# print ss
# print unquote(ss)

# 使用b模式字符串 成功
# cn = b'你好'
# with open('test.txt', 'w') as f:
# 	f.write(cn)


# 获取网络资源
# import requests, json
# url = 'https://api.github.com/repos/solomonxie/gitissues/issues'
# response = requests.request('get', url)
# resp = response.text
# print(type(resp)) # unicode
# print(type('你好')) # str
# print(type( unicode(resp) ))
# print( unicode(resp))


with open('test.txt', 'r') as f:
	src = f.read() # 文件中是"你好"
print(type(src)) # 显示<str>
uni = src.decode('utf-8') # 如果是encode则报错
print(type(uni)) # 显示unicode
# 那么也就是说<str>是bytes类型的了？
# 从外部文件读进来后，是<str>类型，那么写回去是什么类型呢？
with open('test.txt', 'w') as f:
	f.write(src) # 写回去如果是纯英文没问题，只要有ascii之外自负，就必须是<str>类型的，不能是unicode类型否则报错



