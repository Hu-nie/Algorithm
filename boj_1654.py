n, m = map(int, input().split())

arr = list(int(input().strip()) for _ in range(n))

arr.sort()

start = 0
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        total += i //mid
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
