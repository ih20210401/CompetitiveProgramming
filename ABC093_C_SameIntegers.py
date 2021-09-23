import sys
from sys import stdin

input = stdin.readline

A,B,C = map(int, input().split())

ls = []
ls.append(A)
ls.append(B)
ls.append(C)
ls.sort()

maxVal = ls[2]
middleVal = ls[1]
minVal = ls[0]

diff1 = maxVal - middleVal
diff2 = maxVal - minVal

mod1 = diff1 % 2
mod2 = diff2 % 2

ans = 0
if mod1 ==0 and mod2 == 0 :
    ans = (maxVal - middleVal) / 2 + (maxVal - minVal) / 2
elif mod1 == 0 and mod2 == 1 :
    maxVal += 1
    minVal += 1
    ans = 1 + (maxVal - middleVal) / 2 + (maxVal - minVal) / 2
elif mod1 == 1 and mod2 == 0 :
    maxVal += 1
    middleVal += 1
    ans = 1 + (maxVal - middleVal) / 2 + (maxVal - minVal) / 2
else :
    middleVal += 1
    minVal += 1
    ans = 1 + (maxVal - middleVal) / 2 + (maxVal - minVal) / 2

print(int(ans))
