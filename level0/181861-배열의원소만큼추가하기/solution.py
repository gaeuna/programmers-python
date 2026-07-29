def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i]:
            for j in range(arr[i]):
                answer.append(arr[i])
    return answer
