#!/usr/bin/python3
import sys

length = len(sys.argv)

if length < 2:
	print("none")
else:
	print(f"parameters: {length - 1}")
	for i in range(1, length, 1):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")
