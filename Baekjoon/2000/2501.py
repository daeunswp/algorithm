# 약수 구하기

n, k = map(int, input().split())

factors=[]

for i in range(1, n+1):
    if(n%i==0):
        factors.append(i)

if(k > len(factors)): print("0")
else: print(factors[k-1])
    