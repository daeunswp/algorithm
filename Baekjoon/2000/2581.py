# 소수

m = int(input())
n = int(input())

decimal = [True] * (n+2)
decimal[0] = False
decimal[1] = False

actualList = []

sum = 0

for i in range(3, n+1):
    for j in range(2, i):
        if(i%j == 0):
            decimal[i] = False
            break

for x in range (m, n+1):
    if(decimal[x]==True):
        actualList.append(x)
        
for num in actualList:
    sum += num
    
if(sum == 0):
    print("-1")
else:
    print(sum)
    print(actualList[0])