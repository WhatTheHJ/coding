def solution(a, b):
    answer = 0
    
    arr = [a,b]
    arr.sort()
    
    i=a
    
    for i in range (arr[0], arr[1]+1):
        answer += i
        i+=1
    
    return answer