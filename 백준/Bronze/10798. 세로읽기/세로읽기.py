
words = []
result = dict()
get_words = ""

for i in range(5):
    words.append(input())
    
for i in range(15):
    result[i] = ""
    for j in range(5):
        if i < len(words[j]):
            result[i] += words[j][i]
for keys, word in result.items():
    get_words += word
    
print(get_words)