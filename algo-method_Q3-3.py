import sys
from sys import stdin

def solve(N,M,A,B) :
    dp = [[-1 for i in range(M)] for i in range(N)]
    dp[0][0] = 0
    for i in range(N-1) :
        for w in range(M) :
            if dp[i][w] != -1 :
                dp[i+1][w] = max(dp[i+1][w],dp[i][w])
                if w+A[i] < M :
                    dp[i+1][w+A[i]] = dp[i][w] + B[i]
    return dp

input = stdin.readline
N,M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = solve(N,M,A,B)

if dp[N-1][M-1] != -1:
    print(dp[N-1][M-1])
else :
    print(-1)