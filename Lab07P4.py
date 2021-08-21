#Asmita Malakar
#6/23/2021
#Lab 7 Problem 4: Grade Calculator



lab_score_list = []
test_score_list = []

def main():
    number_of_labs = int(input("How many labs? "))
    for i in range(number_of_labs):
        lscore = int(input("Enter a lab score: "))
        lab_score_list.append(lscore)
    print(f"Lab scores: {lab_score_list}")

    number_of_tests = int(input("How many tests? "))
    for i in range(number_of_tests):
        tscore = int(input("Enter a test score: "))
        test_score_list.append(tscore)
    print(f"Test scores: {test_score_list}")
    print("The default weights for course grade are 50% labs and 50% tests.")
    weight_percent_letter = str(input("Enter C to change the weights or D to use default weights: ")).upper()
    if weight_percent_letter == "D":
         grade_calculator(lab_score_list, test_score_list, labPercent=50, testPercent=50)
    elif weight_percent_letter == "C":
        labPercent = int(input("Enter lab percentage (without the % sign): "))
        testPercent = int(input("Enter test percentage (without the % sign): "))
        grade_calculator(lab_score_list, test_score_list, labPercent, testPercent)


def grade_calculator(labList, testList, labPercent = 50, testPercent = 50):
    labNum = 0
    for i in labList:
        labNum = i + labNum
    testNum = 0
    for i in testList:
        testNum = i + testNum

    print(f"Lab average: {labNum/len(labList)}")
    print(f"Test average: {testNum/len(testList)}")

    print(f"Course grade: {((labNum/len(labList)) * labPercent * 0.01) + ((testNum/len(testList)) * testPercent * 0.01)}")




main()

















