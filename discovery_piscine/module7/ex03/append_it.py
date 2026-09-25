#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
	print("none")
	sys.exit()

for i in range(len(sys.argv)):
	if sys.argv[i].find("ism", len(sys.argv[i]) - 3) == -1: # find returns -1 if not found
		print(f"{sys.argv[i]}ism")
