#store three kinds of pizzia names in a list, then use a for loop to print them. 
#print a sentance using the names of the pizzia instead of just the names.
#add a line at the end of your program, outside the for loop.

pizzas = ['pepperoni', 'chicken bacon ranch', 'cheese']
for pizza in pizzas:
    print(f"One of my favorite pizzas is {pizza.title()}")

print(f"\nMy favorite pizza is {pizzas[1].title()}")
print(f"\nMy least favorite pizza is {pizzas[-1].title()} pizza")
print(f"\nMy kids really love {pizzas[0].title()} pizza")
print('\nI really love pizza')