print("Welcome to the Virtual Voting Machine")
n=int(input("enter you age to check your eligibility:"))
if(n>=18):
    print("you can vote,here are the list of candidates whom you can vote:")
    print("1)A")
    print("2)B")
    print("3)C")
    print("4)D")
    a=int(input("Whom do you want to choose?:"))
    if(a==1):
        print("You chose A")
    if(a==2):
        print("You chose B")
    if(a==3):
        print("You chose C")
    if(a==4):
        print("You chose D")
    else:
        print("invalid candidate")
elif(n<18):
    print("Sorry you cant vote")
else:
    print("invalid entry")