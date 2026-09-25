#!/usr/bin/python3

number = input("Give me a number: ")
try:
        number = int(number)
        print("This number is an integer.")
except ValueError:
	try:
		number = float(number)
		print("This number is a decimal.")
	except ValueError:
		print("This number is weird")
