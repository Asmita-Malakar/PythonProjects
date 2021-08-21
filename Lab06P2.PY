# Asmita Malakar
# #June 12, 2021
#Lab 6 Problem 2: Working with lists for skating scores


j_list = []
k_list = []
c_list = []

print("Please enter Jean's scores one by one.")
for i in range(4):
    jeanscore = float(input("Enter a score: "))
    j_list.append(jeanscore)

print(f"Jean's scores: {j_list}")

print("Please enter Kayla's scores one by one.")
for i in range(4):
    kaylascore = float(input("Enter a score: "))
    k_list.append(kaylascore)

print(f"Kayla's scores: {k_list}")


print("Please enter Connie's scores one by one.")
for i in range(4):
    conniescore = float(input("Enter a score: "))
    c_list.append(conniescore)

print(f"Connie's scores: {c_list}")

all_scores = [j_list[:], k_list[:], c_list[:]]
print(f"All scores: {all_scores}")

counter = 0
for score_list in all_scores:
    for i in range(len(score_list)):
        score_list[i] += 1

print(f"All scores after extra point: {all_scores}")

for score_list in all_scores:
    for i in score_list:
        score_list.sort()

print(f"All scores after sorting: {all_scores}")




