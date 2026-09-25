first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
mult = first * second
print(str(first) + " * " + str(second) + " = " + str(mult))
if mult > 0:
	print("The result is positive.")
elif mult < 0:
	print("The result is negative.")
else:
	print("The result is positive and negative.")
