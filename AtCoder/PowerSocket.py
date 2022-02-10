# Input => 4, 10
# 必要な電源タップの個数の最小値を出力

A, B = map(int, input().split())
B += 1
result = B % A

print(result)
