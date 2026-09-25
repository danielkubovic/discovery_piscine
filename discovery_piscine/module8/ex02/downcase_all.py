#!/usr/bin/python3
import sys

def lowercase_it(a):
	return a.lower()

for i in range(1, len(sys.argv)):
	print(lowercase_it(sys.argv[i]))
