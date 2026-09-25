#!/usr/bin/python3
import sys

def shrink(string=None):
	if string is None:
		print("none")
	else:
		print(string[:8])

def enlarge(string=None):
	if string is None:
		print("none")
	else:
		while len(string) != 8:
			string = string + "Z"
		print(string)

for i in range(1, len(sys.argv)):
	if len(sys.argv[i]) > 8:
		shrink(sys.argv[i])
	elif len(sys.argv[i]) < 8:
		enlarge(sys.argv[i])
	else:
		print(sys.argv[i])
