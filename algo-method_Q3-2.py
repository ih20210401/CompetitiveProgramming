import sys
from sys import stdin

input = stdin.readline
N,M = map(int, input().split())

weight = list(map(int, input().split()))

def solve(N,M,weight) :
    dp = [False for i in range(10000+1)]
    for i in range(N) :
        for w in reversed(range(M+1)) :
            
            if dp[w] == True :
                dp[w + weight[i]] = True

            if w == weight[i] :
                dp[w] = True

            if dp[M] == True :
                return True
    return False

ans = solve(N,M,weight)
if ans :
    print("Yes")
else :
    print("No")
