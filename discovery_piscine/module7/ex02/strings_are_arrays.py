#!/usr/bin/python3
import sys

length = len(sys.argv)

if length != 2:
	print("none")
	sys.exit()

z = 0
for i, char in enumerate(sys.argv[1]):
	if char == "z":
		print("z", end = "")
		z += 1
if z == 0:
	print("none")
else:
	print()
