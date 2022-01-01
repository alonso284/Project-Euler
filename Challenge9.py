from math import sqrt
for i in range(1, 1000):
    for n in range(1, 1000):
        if sqrt((i**2)+(n**2)) % 1 == 0 and sqrt((i**2)+(n**2))+i+n == 1000:
            print(i)
            print(n)
            print(sqrt((i**2)+(n**2)))
            print(i*n*sqrt((i**2)+(n**2)))
