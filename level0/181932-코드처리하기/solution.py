def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                answer = answer + code[idx]
            if code[idx] == "1":
                mode = 1
        
        elif mode == 1:
            if code[idx] != "1" and idx % 2 == 1:
                answer = answer + code[idx]
                
            if code[idx] == "1":
                mode = 0
    if len(answer) == 0:
        answer = "EMPTY"
    return answer
