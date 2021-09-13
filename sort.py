N = int(input())
arr = [int(i) for i in input().split()]

for i in range(1,len(arr)) :
    print(' '.join(map(str, arr)))
    val = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > val :
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = val

print(' '.join(map(str, arr)))