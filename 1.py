# -*- coding: UTF-8 -*-
# created by youseatao
"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

count = 0
for i in range(5):
	for j in range(5):
		for k in range(5):
			if i != j and i != k and j != k:
				count += 1

print count