# 소인수분해

# First Try (시간초과)
# num = int(input())

# decimalList=[True]*(num//2+1)
# decimalList[0] = False
# decimalList[1] = False

# primeFactors=[]

# n = num

# for i in range(3, num//2+1):
#     for j in range(2, i):
#         if(i%j == 0):
#             decimalList[i] = False
#             break

# for index, d in enumerate(decimalList):
#     if(d == True):
#         while(True):
#             if(n%index==0):
#                 n = n//index
#                 if(decimalList[n]==True):
#                     break
#             else:
#                 break

# if(num!=1):
#     for p in primeFactors:
#         print(p)

#============================================

# Second Try
num = int(input())

primeFactors = []

for i in range(2, num+1):
    if(num == 1): break
    while(True):
        if(num % i == 0):
            print(i)
            num = num // i
        else:
            break
        


