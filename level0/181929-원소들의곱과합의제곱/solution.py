def solution(num_list):
    total = 1
    total1 = 0
    
    for num in num_list:
        total = total * num
        
    for num2 in num_list:
        total1 = total1 + num2
        
    if total > total1**2:
        answer = 0
    elif total < total1**2:
        answer = 1
        
    return answer
