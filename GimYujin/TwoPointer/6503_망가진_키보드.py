while True:
    m = int(input())

    if m == 0:
        break

    sentence = input()

    keyboard = dict()
    start, end = 0, 0
    answer = 0

    if sentence[start] not in keyboard:
        keyboard[sentence[start]] = 1
    else:
        keyboard[sentence[start]] += 1

    while start <= end and end < len(sentence):
        # print(keyboard)
        # print(start, end)
        if len(keyboard) <= m:
            answer = max(answer, end - start+1)
            end += 1
            if end < len(sentence):
                if sentence[end] not in keyboard:
                    keyboard[sentence[end]] = 1
                else:
                    keyboard[sentence[end]] += 1
        else:
            if keyboard[sentence[start]] <= 1:
                del keyboard[sentence[start]]
            else:
                keyboard[sentence[start]] -= 1

            start += 1

    print(answer)

'''
1
sssss 
-> 5
2
czswabaa
-> 4
'''