#!/usr/bin/python3
num = [2, 8, 9, 48, 8, 22, -12, 2]
num2 = [x + 2 for x in num if x > 5]
num2 = set(num2)

print(num)
print(num2)
