from math import floor
biggest = 0

for i in range(999, 100, -1):
    for n in range(999, 100, -1):
        tempNumber = i * n
        palindrome = list(str(tempNumber))
        try:
            for x in range(0, int(floor(len(palindrome)/2))):
                if palindrome[x] == palindrome[- (x+1)]:
                    continue
                else:
                    raise NameError("not palindorme")
            if tempNumber > biggest:
                biggest = tempNumber
                print(i)
                print(n)

        except NameError:
            continue

print(biggest)
print(tempNumber)
