prime = [2]
currentNumber = 2
while not(len(prime) == 10001):
    currentNumber += 1
    try:
        for p in prime:
            if currentNumber % p == 0:
                raise
        prime.append(currentNumber)
    except:
        continue

print(prime)
