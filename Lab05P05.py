#Asmita Malakar
# 6/30/2021
# nested for loop comparison


names = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]

list1 = [[], [], [], [], [], [], [], []]

for i in range(len(names)):
    for name in names:
        if len(name) > len(names[i]):
            list1[i].append(name)

for a in range(len(list1)):
    print(f"Names longer than {names[a]} are {len(list1[a])}: {list1[a]}")
