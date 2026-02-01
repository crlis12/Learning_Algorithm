import itertools
def solution(s):
    answer = []
    result = []
    
    for i,value in enumerate(s):
        if value not in answer:
            answer.append(value)
            result.append(-1)
        else:
            # print(answer,)
            result.append(len(answer)- (len(answer) - 1 - answer[::-1].index(value)))
            answer.append(value)
            
            
    
    # print(s.index("a"))
    
    return result