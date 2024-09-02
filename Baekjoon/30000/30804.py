#과일 탕후루

n = int(input())
numList = [int(x) for x in input().split()]

nums = numList

largest = 0

firstTmp = nums[0]
secondTmp = 0

indexTmp = 0
removeTmp = 0

while(removeTmp<=n):
    for index, value in enumerate(nums):
        print(secondTmp)
        if(firstTmp != value and secondTmp == 0):
            secondTmp = value
            break
        if(firstTmp!=value and secondTmp!=value):
            if(index-1>largest):
                largest = index-1
            firstTmp = nums[index-1]
            secondTmp = 0
            indexTmp = index
    if(indexTmp != 0):
        for x in range(indexTmp-1, 0):
            if(nums[x] != firstTmp):
                removeTmp = x
                break
        for y in range(0, x-1):
            nums.pop(y)
            
if(len(numList)==1):
    print(1)
else:
    print(largest)