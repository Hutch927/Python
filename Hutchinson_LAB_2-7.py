#Try it yourself 4-11

pizzas = ['pepperoni', 'chicken bacon ranch', 'cheese'] #original list
friends_pizzas = pizzas [:] #Makes a copy of the list
pizzas.append('sausage') #adds to original list
friends_pizzas.append('peppers and onions') #adds to the copied list
print('My favorite pizzas are:') 
for pizza in pizzas: 
    print(pizza.title()) #prints original list with addition
print("My friend's favorite pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza.title()) #prints copied list with addition


#Code from try it yourself 4.1 
#store three kinds of pizzia names in a list, then use a for loop to print them. 
#print a sentance using the names of the pizzia instead of just the names.
#add a line at the end of your program, outside the for loop.
#for pizza in pizzas:
#   print(f"One of my favorite pizzas is {pizza.title()}")
#print(f"\nMy favorite pizza is {pizzas[1].title()}")
#print(f"\nMy least favorite pizza is {pizzas[-1].title()} pizza")
#print(f"\nMy kids really love {pizzas[0].title()} pizza")
#print('\nI really love pizza')