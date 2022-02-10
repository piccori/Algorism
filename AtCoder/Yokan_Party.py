N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split())) + [L]

left = 0
right = L

while right - left > 1:
    mid = (left + right) // 2
    total = 0
    postion = 0
    for a in A:
        if a - postion >= mid:
            total += 1
            postion = A

    if total >= K + 1:
        left = mid
    else:
        right = mid
print(left)
