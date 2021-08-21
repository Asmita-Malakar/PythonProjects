#Asmita Malakar
#June 5, 2021
#Lab 4 Problem 3: Implementing the for loop


#global variables
teamA_score = 0
teamB_score = 0


#for loop to add values from each quarter round
for i in range(4):
    score_A = int(input("Enter team A score in this quarter: "))
    new_scoreA = teamA_score + score_A
    print(new_scoreA)
    score_B = int(input("Enter team B score in this quarter: "))
    new_scoreB = teamB_score + score_B
    print(new_scoreB)
    teamA_score = new_scoreA
    teamB_score = new_scoreB

#deciding which team has won
if teamA_score > teamB_score:
        print("Team A has won")
elif teamB_score > teamA_score:
        print("Team B has won")
else:
        print("It is a tie")



