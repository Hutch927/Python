#create a list of five numbers(integers). use a for loop to iterative over the list and print the sum and product of all the values in the list.

integers = [1, 3, 9, 4, 7] #list of integers
print (f'The list of numbers is {integers}')
product = 1 #setting product to one allowing multiplication in loop

print(f'The sum is: {sum(integers)}')

for integer in integers: #the loop goes over each number and stores the multiplication as the new product. 
	product = product * integer
print(f'The product: {product}')
