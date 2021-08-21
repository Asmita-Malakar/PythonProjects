#Asmita Malakar
# 6/30/2021
#Top score function

import random

top_scores = []
all_scores = []

for i in range(50):
    rand_num = random.randint(0,100)
    all_scores.append(rand_num)
    if len(top_scores) < 5:
        top_scores.append(rand_num)
    elif len(top_scores) == 5:
            if rand_num > min(top_scores):
                top_scores.remove(min(top_scores))
                top_scores.append(rand_num)


print(top_scores)
print(all_scores)