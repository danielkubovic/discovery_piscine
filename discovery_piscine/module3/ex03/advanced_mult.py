#!/usr/bin/python3

'''
i = 0
while i < 10:
	j = 0
	j_results = []
	while j < 10:
		j_result = i * j
		j_results.append(j_result)
		j += 1
	for z in j_results:
		print("Table of",  i, ": ", z)
	i += 1
'''

i = 0
while i < 11:
	print(f"Table of {i}:", end=" ")
	j = 0
	while j < 11:
		print(i * j, end = " ")
		j += 1
	print()
	i += 1
