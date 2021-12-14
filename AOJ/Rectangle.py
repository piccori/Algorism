# 縦 a cm,横 b cm の長方形の面積と周の長さを求めるプログラムを作成
# Input: aとbが１つの空白で区切られて与えられる  /  Output: 面積と周の長さを1つの空白で区切って1行に出力する

# a, b = (int(i) for i in (input().split()))
# print(a * b, (a + b) * 2)

# 他の人の回答
# a, b = map(int, input().split())
# print(a * b, 2 * (a + b))

# map関数の使用例
print(list(map(int, ("1", "2", "3", "4", "5"))))

print(list(map(lambda k: k+k, {"a": 2, "b": 3, "c": 5, "d": 10})))

print(list(map(lambda x: x[0]*x[1], {"a": 2, "b": 3, "c": 5, "d": 7}.items())))

print("".join(map(lambda c: f'{c}"', 'Piccori')))
