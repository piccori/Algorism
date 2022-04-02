period = "."
plus = "+"
dashes = "-"
pipes = "|"


def test(T, R, C):
    total = []
    for i in range(1, T+1):
        total.append(f'Case #{i}\n')

        sum = 0
        while sum <= 2*R[i-1]:
            if sum == 0:
                for j in range((2*R[i-1]+1)+2):
                    if j == 0 or j == 1:
                        total.append(period)
                        continue

                    if j % 2 == 0:
                        total.append(plus)
                        continue

                    total.append(dashes)
                total.append('\n')
                sum += 1
                continue

            if sum == 1:
                for j in range(2*C[i-1]+1):
                    if j == 0 or j == 1:
                        total.append(period)
                        continue

                    if j % 2 == 0:
                        total.append(pipes)
                        continue

                    total.append(period)
                total.append('\n')
                sum += 1
                continue

            if sum >= 2 and sum % 2 == 0:
                for k in range(2*C[i-1]+1):
                    if k % 2 == 0:
                        total.append(plus)
                    else:
                        total.append(dashes)
                total.append('\n')
                sum += 1
            else:
                for k in range(2*C[i-1]+1):
                    if k % 2 == 0:
                        total.append(pipes)
                        continue
                    total.append(period)
                total.append('\n')
                sum += 1

    return total


if __name__ == '__main__':
    T = int(input())
    xy = [map(int, input().split()) for _ in range(T)]
    R, C = [list(i) for i in zip(*xy)]
    result = test(T, R, C)
    print(''.join(result))
