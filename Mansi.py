#program for conversion of temperature from degree celcius to fahrenheit
c=eval(input("enter temperature in degree celcius"))    #temp in degree
f=(c*9/5)+32                                            #conversion
print("corresponding temperature in fahrenheit is ",f)  #temp in fahrenheit

#time format
t=eval(input("enter time in seconds"))      #input
minute=t/60
M=int(minute)                               #integer
hour=t/3600
H=int(hour)                                 #integer
sec=t%60                                    #remender
print("time in required format is ",H,":",M,":",sec)

#name format
myname=eval(input("enter your first name"))
surname=eval(input("enter your surname"))
Mname=eval(input("enter your Mother's name"))
Fname=eval(input("enter your Father's name"))
print(surname,".",myname,"&",Fname,"@",Mname)
print(surname,">",myname,"@",Fname,"#",Mname)

#comparision
a,b=eval(input("enter two numbers"))
if a>b:
    print(a,"is greater than",b)
elif a<b:
    print(a,"is less than",b)
elif a==b:
    print("both numbers are equal")

#even odd
a=eval(input("enter a number"))
if a%2==0:                      #modulus for remender
        print("number is even")
else:
        print("number is odd")

#average of 5 numbers
i=0
s=0
while i<5:
    num=eval(input("enter a number"))
    i=i+1
    s=s+num
print("Average of numbers is ",s/5)

#month name
m_num=eval(input("enter the number between 1 to 12 i.e month number"))
if m_num==1:
    print("january")
elif m_num==2:
    print("february")
elif m_num==3:
    print("march")
elif m_num==4:
    print("april")
elif m_num==5:
    print("may")
elif m_num==6:
    print("june")
elif m_num==7:
    print("july")
elif m_num==8:
    print("august")
elif m_num==9:
    print("september")
elif m_num==10:
    print("october")
elif m_num==11:
    print("november")
elif m_num==12:
    print("december")

#marks to grade
marks=eval(input("enter your marks"))
if 90<=marks<=100:
    print("O")
elif 80<=marks<=89:
    print("A")
elif 70<=marks<=79:
    print("B")
elif 60<=marks<=69:
    print("C")
elif 50<=marks<=59:
    print("D")
elif 40<=marks<=49:
    print("E")
elif marks<40:
    print("F")

#calculator
a,b=eval(input("enter two numbers"))
o=eval(input("enter operator"))
if o=="+":
    print("result= ",a+b)
elif o=="-":
    print("result= ",a-b)
elif o=="*":
    print("result= ",a*b)
elif o=="/":
    print("result= ",a/b)

#Vowels
s1=eval(input("enter a string"))
s2="aeiou"
i=0
for letter in s1:
    if letter in s2:
        i=i+1
        print(letter,i)

#pythagorous theorem
from math import*
print("for a right angle traingle")
a=eval(input("enter a"))
b=eval(input("enter b"))
c=eval(input("enter c"))
a1=pow(a,2)
b1=pow(b,2)
c1=pow(c,2)
if a1+b1==c1:
    print("pythagorous theorem is prooved")



    


            

