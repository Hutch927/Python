#for discussion post 2

high_scores = [200, 100, 99, 75, 60]
print(high_scores)
#Jimmy scores a 150 
high_scores.insert(1, 150)
#We add the score to the second position
print(high_scores)
#We recieve the output: [200, 150, 100, 99, 75, 60]



high_scores_test = [5, 25, 100, 3, 6]
high_scores_test.append(900)
high_scores_test.sort(reverse = True)
print(high_scores_test)

name = input("What is your name? ")
print("Hello", name)