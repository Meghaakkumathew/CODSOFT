a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
o=(input("enter the operator:"))
result=int
if o=='+':
    result=a+b
    print("the sum is:",result)

elif o=='-':
    result=a-b
    print("the difference is:",result)

elif o=='*':
    result=a*b
    print("the product is:",result)

elif o=='/':
    if(b!=0):
        result=a/b
        print("the quotient is:",result)
        
    elif(b==0):
        print("divide by zero error")

else:print("invalid operator!")