#!/usr/bin/python3
import sys

#print(len(sys.argv))

try:
	sys.argv[1]
	if not sys.argv[1] or len(sys.argv) > 2:
		print("none")
	else:
		string = str(sys.argv[1])
		print(string.lower())
except IndexError:
	print("none")
