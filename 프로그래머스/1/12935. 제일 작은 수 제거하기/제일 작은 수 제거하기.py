def solution(arr):
    answer = []
    little = 0
    
    for i in range(len(arr)):
        if arr[i] < arr[little]:
            little = i
            
    if len(arr) == 1:
        answer = [-1]
    else: 
        answer = arr.pop(little)
        answer = arr
    
    return answer