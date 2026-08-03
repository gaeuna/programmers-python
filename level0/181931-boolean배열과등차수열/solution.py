def solution(a, d, included):
    answer = 0
    cnt = 0
    
    for sol in included:
        if sol:
            answer = answer + a + cnt*d
        cnt = cnt + 1
    return answer
