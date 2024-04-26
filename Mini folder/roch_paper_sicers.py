import random
def ai_output():
    n=random.randint(1,3)
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n==3):
        return 3
print("Welcome to the game ")
while(True):
    print("Choose among the three options")
    print("1)ROCK")
    print("2)PAPER")
    print("3)SCISSOR")
    u=int(input())
    b=ai_output()
    if(u==1 and b==2):
        print("ai won*")
    if(u==1 and b==3):
        print("*you won")
    if(u==2 and b==3):
        print("*ai won*")
    if(u==2 and b==1):
        print("you won*")    
    if(u==3 and b==2):
        print("*you won")
    if(u==3 and b==1):
        print("*ai won")
    if(u==b):
        print("Draw")
    i=input("do you want to quit?:")
    if(i=='yes'):
        print("quitting")
        break
    if(i=='no'):
     print("continue to game")
     continue