#설탕배달

num = int(input())

divNum = num%5
divFive = num//5

if(divNum==0):
    print(divFive)
elif(divNum==1 or divNum==2):
    final = 5*(divFive-divNum)+3*(divNum*2)
    if(final==num):
        print((divFive-divNum)+(divNum*2))
    else:
        print(-1)
elif(divNum==3):      
    if(divNum%3==0):
        print(divFive+1)
    else:
        print(-1)
elif(divNum==4):
    final = 5*(divFive-2)+3*(3)
    if(final==num or divFive-2<0):
        print(divFive+1)
    else:
        print(-1)