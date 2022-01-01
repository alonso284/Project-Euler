totalNumber = 0
for i in range(1, 101):
    totalNumber += i*i
print(totalNumber)

number = int((100*101/2)*(100*101/2))
print(number)
totalNumber = number-totalNumber
print(totalNumber)
