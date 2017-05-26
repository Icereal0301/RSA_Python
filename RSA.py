#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# ask判断素数
def aks_sushupanding(n):
	flag = 0
	a = 2
	a1 = pow(a,n,n)
	a2 = pow(a,1,n)
	if a1 == a2:
		return 1
	else:
		return 0

# 取得一个随机素数
def get_suijisushu():
	flag = 0
	while not flag:
		n = random.randrange(2**4095, 2**4096)
		# 剔除部分不可靠因子
		if (n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%13 == 0):
			continue
		flag = aks_sushupanding(n)
	return n

#判断a\b是否互素
def panduanhusu(a,b):
	if a < b:
		a,b=b,a
	while b != 0:
		flag = a%b
		a = b
		b = flag
	if (a,b) == (1,0):
		return 1
	else:
		return 0

# 由欧拉n获得e
def product_e(euler_n):
	flag = 1
	while flag:
		e = random.randrange(2**10,euler_n)
		if panduanhusu(e,euler_n) == 1:
			flag = 0
	return e

def get_d_from_e(a,b):
	flag = b
	if (a < b):
		a,b = b,a
	x2 = 1;x1 = 0; y2 = 0; y1 = 1
	# 乘法逆元(获得乘法逆元的简单算法)
	while (b > 0):
		q = a//b
		r = a -q*b; x = x2 - q*x1; y = y2 - q*y1
		a = b; b = r; x2 = x1; x1 = x; y2 = y1; y1 = y
	if (y2 < 0):
		y2 = flag + y2
	return y2

def RSA_jiami(e,n):
	m = input("输入明文加密： ")
	c = []
	#d = []
	u = []
	o = 0
	for i in m:
		c.append ( pow(ord(i),e,n))
		u.append ( hex(ord(i)))
		#d.append ( hex(pow(ord(i),e,n)))
		o = o + 1

	o = hex(o)
	print ("密文长度为：", o)
	print ("解密后的明文(16进制): ",u)
	print ("密文： ", c)
	return c

def RSA_jiemi(d,n,t):
	m = []
	#h = []
	for i in t:
		m.append( pow(i,d,n))
		#h.append( int('pow(i,d,n)',16))
	a = ''
	for i in m:
		a = a + chr(i)
	#print ('解密后的明文(16进制): ',h)
	print ("解密后的明文: ",a)


# 签名
def RSA_sign(x, d, n):
	y = pow(x,d,n)
	return y

def RSA_ver(x,y,e,n):
	if (x == pow(y,e,n)):
		print ("验证通过")

# RSA整体
def RSA():
	p = get_suijisushu();q = get_suijisushu()
	print('--- p = ',p); print('--- q = ',q)
	n = p * q
	print('--- n = ',n)
	euler_n = (p - 1) * (q - 1)
	print('--- euler_n = ',euler_n)
	e = product_e(euler_n)
	d = get_d_from_e(e, euler_n)
	print("公钥： ",e,n)
	print("私钥： ",d,p,q)
	k = []
	k = input("请输入需要签名的信息：")
	m = []
	for i in k:
		m.append(ord(i))
	x = 0
	for i in m:
		x = x + i
	y = RSA_sign(x,d,n)
	RSA_ver(x,y,e,n)
	t = []
	t = RSA_jiami(e,n)
	RSA_jiemi(d,n,t)


if __name__=='__main__':
	RSA()