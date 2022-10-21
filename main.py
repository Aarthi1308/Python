# """"
# #variable
# a=10
# b=20
# print(a+b)
# print(type(a)) #datatype
# print(id(a)) #memory location
# print(id(b))
 
# #keyword
# # keyword is a reserved words in python 
# # we cannot use a keyword as a variable name,function name,or any other identifier
# # keyword is a case sensitive in python

# import keyword
# print(keyword.kwlist) #all the keywords will be displayed

# #getting input in python

# name=input("Enter your name:")
# print(type(name))
# print(name)

# #cancat the two string
# a=input("Enter your first name:")
# b=input("Enter your last name:")
# print(a+b)

# #adding the two values
# a=int(input("Enter your first name:"))
# b=int(input("Enter your last name:"))
# print(a+b)

# #adding the two decimal values
# a=float(input("Enter your first name:"))
# b=float(input("Enter your last name:"))
# print(a+b)

# #mulitiple inputs in single line
# name1,name2,name3=input("Enter your names:").split(',')
# print("first name:",name1)
# print("second name:",name2)
# print("third name:",name3)
 
# #type casting constructor --- int() str() float()
# a="10"
# print(a)
# print(type(a))
# b=int(a)
# print(type(b))
# print(b)


# #string functions
# a="arthi"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.count(a))
# print(a.endswith("i"))
# print(a.find("r"))
# print(a.replace("arthi","ammu"))
# print(a.isupper())
# print(a.islower())
# print(a.isalnum())
# print(a.isalpha())

# #\n getting a newline
# a="arthi\nis\ngood\ngirl"
# print(a)

# #strip - unwanted space will be removed
# a="      arthi   "
# print(len(a))
# print(len(a.strip()))
# print(len(a.lstrip()))
# print(len(a.rstrip()))

# #string manipulation
# a="arthi"
# print(a[1:])
# print(a[0:4])
# print(a[0:2])
# print(a[-1])
# print(a[::-1]) #reverse the string

# #python operator

# #arithmetic operator
# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b) #floor division
# print(a%b) #modulus
# print(3**3) #exponentiation

# #asignment operator
# a=120
# a+=5
# print(a)
# a-=5
# print(a)
# a*=5
# print(a)
# a/=5
# print(a)


# #relational and comparision operator
# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)


# #logical operator
# a=10
# print(a<=20 and a<=20)
# print(a<=20 or a>=20)
# print(not(a>=20 and a<=20))

# #bitwise operator
# # AND OR NOT

# #if statement

# #write a program to cheack odd no or evne number
# n=int(input("Enter a number:"))
# if (n%2==0):
#     print("Even number:",n)
# else:
#     print("Odd number:",n)  
    
# #if else statement 

# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# if (age>=18):
#     print("eligible for vote")
# else:
#     print("not eligible for vote")   


# #elseif statement 

# marks=int(input("Enter your marks:"))
# if (marks==100):
#     print(" excellant very good score") 
# elif(marks>=80 and marks<=90):
#     print("good") 
# elif(marks>=50 and marks<=70):
#     print("average score") 
# elif(marks>=40 and marks<=50):
#     print("study well") 
# else:
#     print("poor")    
               
# #nested if condition - if condition kulla innu oru if condtion podrathutha nested if


# #while loop

# #print first 10 numbers
# i=1
# while(i<=10):
#  print(i)
#  i += 1
 
#  #print the even numbers
#  i=2
#  while(i<=50):
#      print(i)
#      i+=2
     
# #print the odd numbers
# i=1
# while(i<=20):
#     print(i)
#     i+=2

    
# #break statement

# i=1
# while(i<=10):
#     if(i==6):
#         break
#     print(i)
#     i+=1
   
   
# #range in python

# print(list(range(5)))  
# print(list(range(0,21,2))) 
# print(list(range(1,20,2)))

# #for loop
# #print the first 10 numbers
# for i in range(1,11):
#     print(i) 
    

# #even numbers 2-starting value 21-ending value incerment-2 range=n-1
# for i in range(2,21,2):
#     print(i)      


# #odd numbers
# for i in range(1,20,2):
#     print(i)


# #nested loop
# for i in range(0, 5):
#     for j in range(0, i+1):
#         print("*",end="")
#     print()
    
    
# #while else -- loop complete ah execute aaachuna else part print aagu
# i=1
# while(i<=6):
#     #if(i==3):
#         #break
#     print(i)
#     i+=1
# else:
#     print("loop completed")
    

# #for while 
# for i in range(1,11):
#     print(i)
# else:
#     print("loop completed") 
    
    
# #python lists

# #reassigning the values
# a=[10,20,30,40]
# a[0]=100
# print(a)

# #slicing
# a=[20,40,60,80]
# print(a[1])
# print(a[2])
# print(a[-1])
# print(a[0:3])

# #mulitiple datatypes in single line
# a=[10,"arthi",12.4,True]
# print(a,type(a))
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(type(a[3]))

# #nested list
# a=[10,20,"arthi",10.5,True,[10,20,30]]
# print(a)

# #list methods
# a=[10,20,30,40]
# print(a)
# a.clear()
# print(a) 

# a=[10,20,30] 
# b=a.copy()
# print(b) 

# a=[10,20,30,20,20,30]
# print(a.count(20)) #how many times 20 will be repeated 
# print(a.index(30)) #position of values  
# print(len(a)) 
# print(max(a))
# print(min(a))
# a.pop()
# print(a)
# a.remove(20)
# print(a) 

# a=["arthi"] #inserting the values
# a.append("ammu") 
# a.append("samyu")
# a.append("saje")
# print(a)

# a=["ammu","arthi"] # mergeing the two lists
# b=["samyu","saje"]
# a.extend(b)
# print(a)

# print(list("arthi"))  

# a=[40,60,10,5,20] #assending order
# a.sort()
# print(a)

# a=[10,20,30,40,50] #deseding order
# a.sort(reverse=True)
# print(a)

# a=["z","r","t","a"] #alahabetic order
# a.sort()
# print(a)

# a=["aaa","cccc","a","bb"] #output - a,bb,aaa,cccc
# a.sort(key=len)
# print(a)

# #tuple - values change panna mudiyathu so tuple ah list ah convert pannnitha values change panna mudiyu.
# #a=(10)- epdi tuple la single value kudutha integer nu yeduthuku so namma a=(10,)apdi kudukanu.
# # tuple symbol of ()
# a=(12,12.3,True,"arthi")
# print(a,type(a))

# a=(10,)
# print(a,type(a,))

# a=(10,20,30,40)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])

# #change the value in tuple
# a=(10,20,30,40)
# print(a,type(a))
# b=list(a)
# print(b,type(b))
# b.append(50)
# b=tuple(b)
# print(b,type(b))

# #for loop in tuple
# a=(12,True,"arthi",12.5)
# for i in a:
#     print(i)
    
# #if condition in tuple
# a=("arthi","ammu")
# if "arth" in a:
#     print("arthi is there")
# else:
#     print("arthi is not there") 
    
# #concatinate
# a=(10,20,30,40)
# b=(50,60,70,80)
# print(a+b)

# a=(10,20,30,40,50)
# print(min(a))
# print(max(a)) 

# #nested tuple
# a=(10,20,30,40)
# b=(50,60,70,80)
# print(a,b) 
# print(a[0])
# print(b[1])        

# #set 
# a={1,2,3,4,}
# print(a, type(a))

# #access the value using for loop
# a={10,20,"arthi","ammu"}
# for i in a:
#     print(i)
    
# #remove the values    
# a={"ammu","arthi"}
# a.remove("arthi")
# print(a) 

# a={"ammu","arthi",10,10.5}
# a.clear()
# print(a)

# #union, intersection, symmentric differance - common values ilama erukara values
# a={10,20,30,40,50,60}
# b={50,60,70,50,20,10}
# print(a.union(b))
# print(a.intersection(b))
# print(a.symmetric_difference(b))


# #dictionary
# a={
#     "name":"ammu",
#     "age":21,
#     "place":"covai"
# }
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a["name"])


# user={
#     "name":"ammu",
#     "age":21,
#     "place":"covai"
# }
# for i in user:
#     print(user[i])

# for i in user.keys():
#     print(i)
    
# for i in user.items():
#     print(i) 
    
# if "name" in user:
#     print("name is there")       
 
# #changing the values and update the values
# user.update({"gender":"female"})
# print(user) 

# user["age"]=35
# print(user)


# #identity operator - it identify for same object or not
# # is
# # is not
# a=[10,20]
# b=[10,20]
# c=a
# print(a is c) 
# print(a is b)
# print(a is not b)

# #membership operator
# a=[10,20,30,40]
# print(11 in a)
# print(12 not in a)

# #python function
# def a():
#     print("welcome to function topic")
# a() 
# a()        

# #types of functions
# #no return type without argument function
# def add():
#     a=int(input("Enter the value:"))
#     b=int(input("Enter the value:"))
#     c=a+b
#     print(c)
# add()  

# #no return type with argument function 

# def sub(a,b):
#     print(a-b)
# sub(100,50)     

# #return type without argument function
# def mul():
#     a=int(input("Enter the value:"))
#     b=int(input("Enter the value:"))
#     c=a*b
#     return c
# x=mul()
# print(x)

# #return type with argument function
# def div(a,b):
#     return a/b
# x=div(100,20) 
# print(x)

# #arbitrary arguments function - n mnuber of arguments will be stored
# def a(*students):
#     print(students)
#     for i in students:
#      print(i) 
# a("arthi","ammu","samyu","saje") 

# #keyword argument function
# def detail(name,age,location):
#     print("my name is",name,"my age is",age,"i am coming from",location)
# detail(name="arthi",location="coimbatote",age=21)

# #arbitrary keyword argument function -- using two stars(**)        
# #n number of keyword argumnets will be stored

# #default parameter function
# def user_1(name,city="chennai"):
#     print(name,"from",city)
# user_1("arthi","coimbatore")
# user_1("ammu")   
 
# #recursion function 
# def factorial(n):
#   if n == 1:
#       return n
#   else:
#       return n * factorial(n-1)    
# print(factorial(5)) 

# #lambda function
# a=lambda b:b+50
# print(a(5))

# a=lambda b,c:b*c
# print(a(10,2))

# #date time package in python
# import datetime as dt
# date=dt.date.today() 
# print("current date:",date)

# #update date
# new=dt.date(2022,8,13)
# print(new)
# print(new.year)
# print(new.month)
# print(new.day)

# #time
# a=dt.time(10, 45, 40, 4000)
# print(a)
# print(a.hour)
# print(a.minute)
# print(a.second)

# #current time
# a=dt.datetime.now()
# print(a)

# #differance between one date to another date
# a=dt.datetime.now()
# b=dt.datetime(2021,10,22)
# c=a-b
# print(c)

# #string format in date
# a=dt.datetime.now()
# b=a.strftime("%A %B %d %Y")
# print(b)

# #math function
# import math
# print(math.sqrt(4))
# print(math.ceil(1.555))
# print(math.floor(1.555))
# print(math.factorial(5))
# print(math.pow(2,3))
# print(math.pi)

# #type of error
# #compli time error - (: , / ;)
# #run time error    -(syntax error)

# #try block in python
# #a=10/0
# #print(a)

# try:
#  a=10/0
# except Exception as e: 
#  print(e)
 
# #try except else in python 
# try:
#  a=10/50
# except Exception as e: 
#  print(e)
# else:
#     print("A value is:",a)
    
# #try except else finally in python     
# try:
#  a=10/50
# except Exception as e: 
#  print(e)
# else:
#     print("A value is:",a)
# finally:
#     print("exception eruthalu ilainalu finally la ludukarathu print aagu")
  
# #types of exception 
# #name error exception
# try: 
#  print(a) 
# except NameError as n:
#     print("a is not defined") 
    
# #zero division error
# try: 
#    a=10/0 
# except ZeroDivisionError as n:
#     print("denominator can't be zero") 
    
# #value error
# try:
#   a=int("arthi")
# except ValueError as n: 
#  print("please enter only integer values")
 
# #index error
# try:
#   a=[10,20,30,40]
#   print(a[10])
# except IndexError as n: 
#  print("invalid index")  
 
# #file not found error
# try:
#     f=open("text.txt")
# except FileNotFoundError:
#     print("file not found")
# else:
#     print(f.read())         
 
# #handling multiple exception
# try:
#     a=10/25
#     print(a)
#     b=[10,20,30]
#     print(b[10])
#     c=int("ammu")
#     print(c)
# except ZeroDivisionError:
#     print("ZeroDivisionError") 
# except IndexError:
#     print("index error")
# except ValueError:
#     print("value error")    
# """
# #oops concept in python                    