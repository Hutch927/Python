#make a list of the first 10 cubes and use a for loop to print the value of each cube

cubes = []

for value in range (1, 11):
	cubes.append(value**3)
	print(cubes [-1])
	