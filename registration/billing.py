#Asmita Malakar and Sarah Tolman
# 07/18/201
# Course Registration System - Billing System


def calculate_bill(id,i_s_list,r_list,h_list):
    cost = 0
    enrolled_list = []
    for i in r_list:
        if id in i:
            index = r_list.index(i)
            enrolled_list.append(h_list[index])

    # Calculating total credit hours
    Sum = sum(enrolled_list)
    if id in i_s_list:
        #In-state tuition
        cost = Sum * 225
    elif id not in i_s_list:
        #out-of-state tuition
        cost = Sum * 850


    display_hours_and_bill(Sum, cost)



def display_hours_and_bill(hours, cost):
    print(f"Course load: {hours} credit hours")
    print(f"Enrollment cost: ${cost}")









