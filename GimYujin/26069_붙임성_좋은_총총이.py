N = int(input())
dancePeople = set()
for _ in range(N):
    person1, person2 = input().strip().split(" ")
    if person1 in dancePeople or person2 in dancePeople:
        dancePeople.add(person1)
        dancePeople.add(person2)

    if person1 == "ChongChong" or person2 == "ChongChong":
        dancePeople.add(person1)
        dancePeople.add(person2)

print(len(dancePeople))
