def solution(x):
    answer = False
    a= 0
    
    int(x)
    b=list(str(x))
    
    for i in range (len(b)):
        a += int(b[i])
        
    if int(x)%a == 0:
        answer = True

    return  answer