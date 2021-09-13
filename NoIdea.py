n,m = map(int,input().split())

listOriginal=list(map(int,input().split()))
set_original = set(listOriginal)

set_A = set(input().split(' '))
set_B = set(input().split(' '))

score = 0

for val in set_original :
    if val in set_A :
        score += 1
    if val in set_B :
        score -= 1

print(score)
