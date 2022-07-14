N = int(input())
words = []

for _ in range(N):
    words.append(input())

words = list(set(words))

for i in range(len(words) - 1):
    for j in range(i + 1, len(words)):
        if len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]

        elif len(words[i]) == len(words[j]):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]

for word in words:
    print(word)

    
N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append((word, len(word)))

words = list(set(words))

words = sorted(words, reverse = False, key = lambda word : (word[1], word[0]))

for word in words:
    print(word[0])