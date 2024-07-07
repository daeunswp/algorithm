# 약수들의 합
numList = []

while(True):
    num = int(input())
    if(num == -1):
        break
    numList.append(num)

for n in numList:
    total = 1
    divisor = '= 1'
    for i in range(2, n):
        if(n%i==0):
            total += i 
            divisor += ' + '
            divisor += str(i)
        else:
            continue
       
    if(total == n):
        print(n, divisor)
    else:
        print(n, "is NOT perfect.")
        
        
            