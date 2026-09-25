#!/usr/bin/python3
import sys

#print(len(sys.argv))

try:
	sys.argv[1]
	if len(sys.argv) != 3:
		print("none")
	else:
		print(sys.argv[2].count(sys.argv[1]))
except IndexError:
	print("none")
