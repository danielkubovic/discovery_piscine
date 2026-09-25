#!/usr/bin/python3
import sys

#print(len(sys.argv))

length = len(sys.argv)

if length < 2:
	print("none")
else:
	for i in range(length - 1, 0, -1):
		print(sys.argv[i])

'''
	i = length
	while i != 0:
		print(sys.argv[i - 1])
		i = i - 1
'''
