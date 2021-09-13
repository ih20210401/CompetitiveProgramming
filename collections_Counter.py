
# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(input())
ls = list(map(int,input().split()))
num2 = int(input())

sum = 0
for i in range(num2) :
    key,value = map(int,input().split())

    if key in ls :
        sum += value
        ls.remove(key)

print(sum)
