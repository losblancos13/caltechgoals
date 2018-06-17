sec=eval(input("Enter time in Seconds: "))
a=sec//60
b=sec%60
if a<60&b<60:
        print("Time is- 00:",a,":",b)
elif a<60&b>60:
        print("Time is- 00:",a+(b//60),":",b%60)
elif a>60&b<60:
        print("Time is- ",a//60,":",a%60,":",b)
else:
        print("Time is- ",a//60,":",(a%60)+(b//60),":",b%60)
        

