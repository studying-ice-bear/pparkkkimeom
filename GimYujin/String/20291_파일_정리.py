from collections import defaultdict
N = int(input())

file_system = defaultdict(int)

for _ in range(N):
    filename, filetype = input().split('.')
    file_system[filetype] += 1


for name, type in sorted(file_system.items(), key=lambda x: x[0]):
    print(name, type)
