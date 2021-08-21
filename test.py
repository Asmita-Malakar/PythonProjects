def cf(num1,num2):
    n = []
    for i in range(1, 10000001):
        if num1%i==num2%i==0:
            n.append(i)

    return n

print(cf(5,10))


