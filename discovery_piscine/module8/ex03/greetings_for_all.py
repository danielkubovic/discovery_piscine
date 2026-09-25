#!/usr/bin/python3

def greetings(a="noble stranger"):
	if isinstance(a, str):
		print(f"Hello, {a}")
	else:
		print("Error! It was not a name.")


greetings("John")
greetings()
greetings(42)
