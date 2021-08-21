#Asmita Malakar
# 6/30/2021
# printing list with random values


import random


def create_list():
    max_len = 50
    my_list = []
    for i in range(max_len):
        my_list.append(random.randint(1, 99))

    print(my_list)

create_list()