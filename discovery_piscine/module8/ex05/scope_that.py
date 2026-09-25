#!/usr/bin/python3

def add_one(a):
	a += 1
	return a
a = 5
print(a)
print(add_one(a))
print(a)

'''
# x = local scope
def secret():
	x = 5
	return x
secret()
print(x)
'''

'''
# x = global scope
def secret():
	return x
x = 5
print(secret())
'''

'''
# x = local scope, which includes it's functions
def fun():
	x = 5
	def secret():
		print(x)
	secret()
fun()
'''
'''
# x = global scope in local scope, thanks to "global"
def fun():
	global x
	x = 5
fun()
print(x)
'''
