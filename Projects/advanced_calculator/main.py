from operations import add,sub,exp,div,mul
his=[]
def menu():
    print("Advanced Calculator\n")
    print("Enter your choice: ")
    print("1 for add\n2 for subtraction\n3 for product\n4 for exponent\n5 for division\n6 for history\n7 fo exit:")

while True:
    menu()
    c=int(input())
    if c==7:
        print("Exiting calculator")
        break
    if c==6:
        for item in his:
            print(item)
        continue
    try:
        x=float(input("Enter first number: "))
        y=float(input("Enter second number: "))
            
        if c==1:
                print("Sum is: " ,add(x,y))
        elif c==2:
                print("Difference is: ",sub(x,y))
        elif c==3:
                print("Product is: ",mul(x,y))
        elif c==4:
                print("Exponent is: ",exp(x,y))
        elif c==5:
                print("Division is: ",div(x,y))
    except ValueError as e:
        print("Error",e)