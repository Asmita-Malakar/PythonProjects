string = "i_love_programming_in_python_and_i_will_alzways_program"
string_list = []

for a in string:
    string_list.append(a)


for i in string_list:
    if string_list.count(i) == 1:
        print(i)
    else:
        continue