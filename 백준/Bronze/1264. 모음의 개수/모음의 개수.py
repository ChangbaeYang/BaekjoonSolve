import sys
input = sys.stdin.readline

mooum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    word = input()
    if word == '#\n':
        break
        
    count = 0
    for w in word:
        if w in mooum:
            count += 1
    print(count)