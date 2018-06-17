a,b=eval(input("Enter two numbers: "))
o=str(input("What operation do you want to perform: "))
if o=="+":
        print("You chose to add the two numbers: ")
        print("The sum is: ",a+b)
if o=="-":
        print("You chose to subtract second number from first numbr: ")
        print("The difference is: ",a-b)
if o=="*":
        print("You chose to multiply two numbers: ")
        print("The multiplications is: ",a*b)
if o=="/":
        print("You chose to divide the first number by second number: ")
        if b==0:
                print("Division by zero not possible")
        else:
                print("The division is: ",a/b)

