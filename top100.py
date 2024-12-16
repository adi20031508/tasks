#even or odd
n= int(input("enter the number"))
sum=0
for i in range(n+1):
    sum+=i
print(sum)
if(sum%2 == 0):
    print("even")
else:
    print("odd")
#positive negative
n= int(input("enter the number:"))
if(n >0):
    print("the number is positive")
else:
    print("the number is negative")
#sum of natural numbers
n=8
sum=0
for i in range(n+1):
 sum+=i
print(sum)
#sum of natural numbers
n=int(input("enter the number: "))
sum=0
for i in range(n+1):
    sum+=i
print(sum)
#sum in given range
a=2
b=5
sum=0
for i in range(a , b+1):
 sum+=i
print (sum)
#greater among two
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if(a>b):
   print("a is greater number")
else:
   print("b is greater number")
#greatest amon three
a=20
b=30
c=20
if(a>=b & a>=c):
   print(a)
   if(b>=a & b>=c):
      print(b)
   else:
      print(c)
#leap year
n=2000
if(n%4==0 & n%100 !=0) or (n%400==0):
   print("the year is leap year")
else:
   print("its not")
#prime number
n=11
flag = 0 #assuming not prime
for i in range(2,n):
   if(n%i==0):
      flag=1 #its prime
      break
if(flag ==1):
      print("not prime")
else:
      print("prime")
#prime in given range
l=2
h=10
prime=[]
for i in range(l, h+1):
   for j in range(2,i):
      if(i%j==0):
         break
   else:
    prime.append(i)
print(prime)
#sum of digits
n=(1,2,2,3)
sum=0
for i in n:
   sum+=i
print(sum)
#reversing the number
numbers=int(input("enter the digits:"))
while(numbers>0):
   
   
   

   
   
      
      
   