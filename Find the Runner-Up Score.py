n = int(input())
arr = map(int, input().split())

arr = sorted(arr)

for i in range(len(arr)-1, -1, -1):
    if arr[i] != arr[-1]:
        print(arr[i])
        break