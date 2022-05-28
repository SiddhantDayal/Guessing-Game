import random
def hint(x):
    a=[]
    for i in range(1, x + 1):
       if x % i == 0:
           a.append(i)
    #print(a)
    c=random.choice(a)      
    y=random.randint(1,3)
    if (y==1):
            print("It is a multiple of",c)
    if (y==2):
            print("It is greater than",random.randint(0,x))
    if( y==3):
            print("It is lesser than",random.randint(x,100))
print("Welcome to the guessing Game!")
x=random.randint(0,100)
print("Can You guess the number between 1 and 100")
score=10
while(True):
    g=int(input())
    if (g==x):
        print("You are Right, and your score is,",score)
        break
    else:
        print("You are wrong")
        hint(x)
        score-=1
        continue
