# Write a program that asks for a decimal number as input and outputs the froogon representaiton of that number.
# The froogon representation of a number is the sum of the digits after the number multiplied by the factorial of the position of the digit was calculated.

# Input: A single decimal number N, in decimal notation.
# Output: N written in froogon notation.

# Example: 13 in froogon notation is 1 0 2          (1 * 1! + 0 * 2! + 2 * 3!)
# Example: 17 in froogon notation is 1 2 2          (1 * 1! + 2 * 2! + 2 * 3!)
# Example: 24 in froogon notation is 0 0 0 1        (0 * 1! + 0 * 2! + 0 * 3! + 1 * 4!)

import math

def isValid(number, froogon):
  value = 0
  for i, v in enumerate(froogon):
    value += v * math.factorial(i+1)
  return value == number

factorials = [1, 1] #0!, 1!
for i in range(2, 25):
       factorials.append(factorials[-1] * i)
n = int(input())
a = 1 #index of smallest factorial > n
while n >= factorials[a]:
       a += 1
foo = [0 for i in range(a)]
for i in range(a-1, -1, -1): # for every factorial less than a!
       while(n >= factorials[i]): # represent as much of n as possible
               foo[i] += 1
               n -= factorials[i]
print(" ".join(map(str,foo[1:])))