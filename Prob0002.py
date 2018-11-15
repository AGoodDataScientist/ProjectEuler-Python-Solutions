# -*- coding: utf-8 -*-
"""
Project Euler Problem 2: Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
def FibEvenSum():
    sumval = 0
    TotVal = 0
    i=2
    PrevNum = 1
    while i < 4000000:
        sumval = PrevNum + i
        if i%2 == 0:
            TotVal += i
        PrevNum = i
        i = sumval
    return(TotVal)

if __name__ == "__main__":
    print(FibEvenSum())
        