m= int(input("Enter the MPL marks"))
operator = input("Enter operator: ")
n= int(input("Enter TOA marks"))
operator = input("Enter operator: ")
p = int(input("Enter Basic Electronic marks"))
ob=m+n+p
x=int(input("enter total num"))
percentage = x/ob*100
if operator == "+":
    print(m+n+p)
    print(percentage)
elif operator == "-":
    print(m-n-p)
elif operator == "*" or operator == "x":
    print(m*n*p )
elif operator == "/":
    print(m/n/p)


  
  
    





    