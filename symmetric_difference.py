# Enter your code here. Read input from STDIN. Print output to STDOUT

num1 = input()
set1 = set(list(input().split()))

num2 = input()
set2 = set(list(input().split()))

resultSet = set1.symmetric_difference(set2)

print(len(resultSet))
