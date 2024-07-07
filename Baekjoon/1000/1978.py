#소수 찾기
#2~1000까지 for문을 돌아 소수인지 아닌지를 먼저 판별하고 들어온 값과 비교

count = int(input())
number = map(int, input().split())
decimalCount = 0

decimalList = [True] * 1002
decimalList[0] = False
decimalList[1] = False

for i in range(3, 1001):
    for j in range(2, i):
        if(i%j == 0):
            decimalList[i] = False
            break
                
for n in number:
    if(decimalList[n]==True):
        decimalCount += 1

print(decimalCount)
                        
        

            
        