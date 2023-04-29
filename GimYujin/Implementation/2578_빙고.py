graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

shout = []
for i in range(5):
    shout.append(list(map(int, input().split())))


def check():
    yeah = 0
    left_diagonal = 0
    right_diagonal = 0
    for i in range(5):
        row = 0
        column = 0
        for j in range(5):
            if i == j and bingo[i][j] == 1:
                right_diagonal += 1
            if i+j == 4 and bingo[i][j] == 1:
                left_diagonal += 1

            if bingo[i][j] == 1:
                row += 1

            if bingo[j][i] == 1:
                column += 1

        if row == 5:
            yeah += 1

        if column == 5:
            yeah += 1

    if right_diagonal == 5:
        yeah += 1

    if left_diagonal == 5:
        yeah += 1

    if yeah >= 3:
        return True

    return False


bingo = [[0] * 5 for _ in range(5)]
flag = False

for i in range(5):
    for j in range(5):
        x = shout[i][j]
        for a in range(5):
            for b in range(5):
                if x == graph[a][b]:
                    bingo[a][b] += 1
                    break
        # print(i, j)
        # print(*bingo, sep="\n")
        if check():
            # print("bingo!")
            flag = True
            break
    if flag:
        break

count = 0
for i in range(5):
    for j in range(5):
        if bingo[i][j] == 1:
            count += 1

print(count)


'''
bingo = [
    [1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1]
]

yeah = 0
left_diagonal = 0
right_diagonal = 0
for i in range(5):
    row = 0
    column = 0
    for j in range(5):
        if i == j and bingo[i][j] == 1:
            right_diagonal += 1
        if i + j == 4 and bingo[i][j] == 1:
            left_diagonal += 1

        if bingo[i][j] == 1:
            row += 1

        if bingo[j][i] == 1:
            column += 1

    if row == 5:
        yeah += 1

    if column == 5:
        yeah += 1

if right_diagonal == 5:
    yeah += 1

if left_diagonal == 5:
    yeah += 1

print(*bingo, sep='\n')
print(yeah)
'''

'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
1 7 13 19 25
5 9 17 21 6
11 16 2 3 4
8 24 10 12 14
15 18 20 22 23

'''