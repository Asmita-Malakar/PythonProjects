# Asmita Malakar
# #June 12, 2021
#Lab 6 Problem 1: Checking for values under 60 and replacing them


test_score = []


for i in range(5):
    score = float(input("Enter a test score: "))
    test_score.append(score)

print(f"All scores: {test_score}")

new_test_score = test_score.copy()
less_than_sixty_value = 10
more_than_sixty_value = 0

counter = 0
for i in new_test_score:
    if i < 60:
        i += 10
    new_test_score[counter] = i
    counter = counter + 1

print("Students who scored below 60 get 10 extra points.")
print(f"All scores: {new_test_score}")

print("Students whose scores have changed:")
value = 0
for i in new_test_score:
    if test_score[value] != new_test_score[value]:

        print(f"Old score: {test_score[value]} New Score: {new_test_score[value]}")
    value = value + 1





