n=37
while(True):
    a=int(input("Enter a number between 20 and 50:"))
    if(a!=n and a>30 and a<40):
        print("you guessed wrong guess again[Hint think of a number greater than 35 and less than 40]")
    if(a==n):
        print("you guessed the right number")
        break
    if(a>=25 and a<30 or a>40 and a<50 ):
        print("think again")