def solution(n):
    answer = []
    answer = str(n).split()
    result = sorted(answer[0],reverse=True)
    # for i in range(len(n)):
    #     answer.append(int(i))
    return int("".join(result))