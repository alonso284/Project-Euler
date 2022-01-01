# https://projecteuler.net/problem=3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
largestPrime = 0

while largestPrime == 0:
    for n in range(2, number + 1):
        if n == number:
            largestPrime = n
        elif number % n == 0:
            print(int(number/n))
            number = int(number/n)
            break

print(largestPrime)
