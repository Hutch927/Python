filename = 'History_of_Norwich.txt'

with open(filename) as file:
    lines = file.readlines()

with open(filename, "r+") as file:
    for line in lines:
        file.write(line.replace('Patidge', 'Partridge'))

