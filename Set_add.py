# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())

s = set()

for i in range(num) :
    val = input()
    if not val in s :
        s.add(val)

print(len(s))