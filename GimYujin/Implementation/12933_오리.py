from collections import deque
sound = list(s for s in input())
ducks = deque()

for i in range(len(sound)):
    # print(i, sound[i], ducks)
    if not ducks:
        ducks.append([sound[i]])
    else:
        check = True
        for j in range(len(ducks)):
            if ducks[j][-1] == "q" and sound[i] == "u":
                ducks[j].append("u")
                check = False
                break
            elif ducks[j][-1] == "u" and sound[i] == "a":
                ducks[j].append("a")
                check = False
                break
            elif ducks[j][-1] == "a" and sound[i] == "c":
                ducks[j].append("c")
                check = False
                break
            elif ducks[j][-1] == "c" and sound[i] == "k":
                ducks[j].append("k")
                check = False
                break
            elif ducks[j][-1] == "k" and sound[i] == "q":
                ducks[j].append("q")
                check = False
                break

        if check:
            if sound[i] == "q":
                ducks.append(["q"])
            else:
                ducks.append([sound[i]])
                break

answer = 0

for i in range(len(ducks)):
    if ducks[i][-1] == "k" and len(ducks[i]) >= 5:
        answer += 1
    else:
        answer = -1
        break

print(answer)

'''
"quack"
quqacukqauackck
qu_ac_kq_ua__ck
__q__u__a__ck
2

quqaquuacakcqckkuaquckqauckack
qu_a____c_k_q___u_
__q__u_a___c__k_
____q_u__a___c_k
3

ququackakc
-1

quackkk
-1

quackqu
-1

qquacku
-1
'''