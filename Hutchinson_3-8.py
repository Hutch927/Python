#this code is from  3-8 'try it yourself' on page 46
places = ['ireland', 'scotland', 'england', 'alaska', 'costa rica']

print("Here is the original list:") #trying to make the output cleaner
print(places) #prints an unformated version of the list

print('\nHere is the list sorted alphabetically:')
print(sorted(places)) 

print('\nHere is the original list again:') #printing the original list again to show that it was not altered
print(places)

print('\nHere is the list sorted in reverse order') 
print(sorted(places, reverse=True)) #prints in reverse alphabetical order

print('\nHere is the original list again:') 
print(places)


print('\nHere is the list in reverse order:')
places.reverse() #flips the list
print(places)

print('\nHere is the list back to the original order:')
places.reverse() #reverting back to original list
print(places)

print('\nHere is the list sorted again:')
places.sort() #sorting the list
print(places)

print('\nHere is the list sorted in reverse:')
places.sort(reverse=True)
print(places)

