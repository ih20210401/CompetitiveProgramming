import sys
from sys import stdin

input = stdin.readline
N = int(input())

def rec(cur,use) :
    global counter
    if N < cur :
        return
    if use == 0b111 :
        counter += 1

    rec(7+cur*10,use | 0b001)
    rec(5+cur*10,use | 0b010)
    rec(3+cur*10,use | 0b100)

counter = 0
rec(0,0)
print(counter)
