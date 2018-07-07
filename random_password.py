#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import datetime,hashlib

#Get now datetime 'm-d-y h:m:s' as a str
Now = datetime.datetime.now().strftime('%D %T')
#Hash the datetime use sha512 , output as hex str
HashValue = hashlib.sha512(Now.encode('UTF-8')).hexdigest()

#Use hash result creat the password (only numbers)
#PasswdBit = ''
PasswdBit = input('请输入需要的密码位数: ')
while True:
	if PasswdBit.isdigit():
		break
	else:
		print('只能输入数字，请重新输入')
		PasswdBit = input('请输入需要的密码位数: ')

Passwd = ''

while len(Passwd) != int(PasswdBit):
	for i in HashValue:
		if i.isdigit():
			Passwd = Passwd+i
		if len(Passwd) == int(PasswdBit):
			break

print('您的随机密码是：%s'%(Passwd))



