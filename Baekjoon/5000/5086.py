# 배수와 약수

aList = []
bList = []


while(True):
    a, b = map(int, input().split())
    if(a == 0 and b==0):
        break
    else:
        aList.append(a)
        bList.append(b)

# list의 index와 item을 받아오려면 enumerate를 쓰면 된다!
for index, a  in enumerate(aList):
     
    if(a % bList[index] == 0):
        print("multiple")
    elif(bList[index] % a == 0):
        print("factor")
    else:
        print("neither")