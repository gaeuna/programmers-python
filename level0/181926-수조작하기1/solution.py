def solution(n, control):
    for i in range(len(control)):
        if "w" in control[i]:
            n = n + 1
        if "s" in control[i]:
            n = n - 1 
        if "d" in control[i]:
            n = n + 10
        if "a" in control[i]:
            n = n - 10
    answer = n
    return answer
