#Asmita Malakar
# June 16, 2021

prices = [10,130,25, 64,91,66,42,18,141,64]
filtered_list = []

for i in prices:
    if 20 < i < 80:
        filtered_list.append(i)

print(filtered_list)
