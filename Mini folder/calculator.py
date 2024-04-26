print("Your calculator")
print("operations")
print("1.Add")
print("2.Sub")
print("3.Multiple")
print("4.Divide")
print("5.Remainder")
print("6.Power")
n=int(input())
a=int(input("give first number:"))
b=int(input("give second number:"))
while(True):
  if(n==1):
    print(f"sum is {a+b}")
    break
  if(n==2):
    print(f"difference is {a-b}")
    break
  if(n==3):
    print(f"multiplication is {a*b}")
    break
  if(n==4):
    print(f"division is {a//b}")
    break
  if(n==5):
    print(f"remainder is {a%b}")
    break
  if(n==6):
    print(f"power is {a**b}")
    break
  else:
    print("invalid input")
    break
print("thanks for using it")