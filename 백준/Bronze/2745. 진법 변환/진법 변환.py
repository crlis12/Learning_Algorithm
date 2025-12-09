str_num, num = input().split()
base = int(num)
result = 0

for i in range(len(str_num)):
    ch = str_num[i]

    if '0' <= ch <= '9':          # 숫자
        value = ord(ch) - ord('0')
    else:                         # 알파벳
        value = ord(ch) - ord('A') + 10

    result += value * (base ** (len(str_num) - i - 1))

print(result)
