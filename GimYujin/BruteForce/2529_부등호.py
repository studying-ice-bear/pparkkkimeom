k = int(input())
A = list(input().split(' '))
total = []

def bruteForce(num, cnt):
    if cnt == k:
        # print(*numbers)
        total.append(numbers.copy())
        return

    if A[cnt] == '<':
        for j in range(10):
            if num < j and not check[j]:
                check[j] = True
                numbers.append(j)
                bruteForce(j, cnt+1)
                check[j] = False
                numbers.remove(j)
    else:
        for j in range(10):
            if num > j and not check[j]:
                check[j] = True
                numbers.append(j)
                bruteForce(j, cnt+1)
                check[j] = False
                numbers.remove(j)


for i in range(10):
    check = [False for _ in range(10)]
    numbers = [i]
    check[i] = True
    bruteForce(i, 0)

print(*total[-1], sep="")
print(*total[0], sep="")
