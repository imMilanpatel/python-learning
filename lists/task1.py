# Challenge: You are in charge of sorting test scores for an exam.
# There are some results missing as in the following points:

# Test Score inputs
score = [100, 5, 10, 25, 3, 22]

# Add the integer 1 to any position in the list
score.insert(3,1)

# Add the integer 50 to the end of the list
score.append(50)

# Add the list 45, 33, 16 to the end of the list
score += 45,33

# then sort the list so it is ordered largest number to smallest
# (eg 100, 50, 45, 33, 25, 22, 16, 10, 5, 3, 1)
score.sort(reverse=True)
assert(score == [100, 50, 45, 33, 25, 22, 16, 10, 5, 3, 1])

# Print the first score in the list to declare the winner of the exam.
print("The Winner is with the score of",max(score))