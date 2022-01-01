number = []
for i in range(1, 21):
    number.append(i)


def mcd(n, m):
    mcd = 1
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            mcd = i
    return(mcd)


totalNumber = 1
for i in number:
    divisor = mcd(totalNumber, i)
    totalNumber = int(totalNumber/divisor) * int(i/divisor) * divisor

print(totalNumber)
