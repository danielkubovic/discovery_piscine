#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
	print("none")
	sys.exit()

check = input("What was the first parameter? :")
if check == sys.argv[1]:
	print("Good job!")
else:
	print("Nope, sorry...")
