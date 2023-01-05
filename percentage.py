# p1=40
# p2=56
# p3=60
# total=p1+p2+p3
# per=total/3.0
# print(per)

# name='darshan'
# print(name[:5])
# print(name[:])
# print(name[1:5:2])

# print(float(3))
# # print(float(50+2j))
# print(float(True))
# print(float(False))
# print(float("4"))

# mylist=['darshan','shubham','nishad','rohan','mohan']
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:4])

# mytuple=('darshan','shubham','nishad','rohan','mohan',2,3,4)
# print(mytuple)
# # mytuple[1]="hello"

# myset={10,20,30,40}
# yourset={30,40,50,60}
# print(myset.union(yourset))
# print(myset.intersection(yourset))
# print(myset.difference(yourset))

# mydic={
#     101:'darshan',102:'shubham',103:'nishad',104:'rohan'
# }
# print(mydic[101])
# it is mutable
# a,b,c,d=map(int,input().split())

# if(a>b and a>c and a>d):
#     print(a,'is largest number')
# if(b>a and b>c and b>d):
#     print(b,'is largest number')
# if(c>b and c>a and c>d):
#     print(c,'is largest number')
# if(d>b and d>a and d>c):
#     print(d,'is largest number')


# if(a<b and a<c and a<d):
#     print(a,'is smallest number')
# if(b<a and b<c and b<d):
#     print(b,'is smallest number')
# if(c<b and c<a and c<d):
#     print(c,'is smallest number')
# if(d<b and d<a and d<c):
#     print(d,'is smallest number')

# p1,p2,p3,p4,p5=map(int , input().split())
# print(p1,p2,p3,p4,p5)
# ch=input()
# if ch.isupper():
#     print('yes')
# else:
#     print('no')
# arr=[2,3,4,5,6,7,8,9,10]


# for i in range(1,11):
#     print(i*arr[0] ,"  " ,i*arr[1],"  " ,i*arr[3],"  " ,i*arr[4],"  " ,i*arr[5],"  " ,i*arr[6],"  " ,i*arr[7],"  " ,i*arr[8],'  ')
    

# name =input()
# for i in range(len(name)):
#     if (name[i]=='n'):
#         print("index",i)
        
# for i in range(1,6):
#     print(i,"  ",6-i)
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if(i==3 and j==3):
#         continue
#     print(i,"  ",j)

# print('1.add')
# print('2.sub')
# print('3.mul')
# print('4.div')
# c=int(input('enter your choice:'))
# n1=int(input('enter your first no:'))
# n2=int(input('enter your second no:'))
# while True:
#     if(c==1):
#         print('result',n1+n2)
#         break
#     if(c==2):
#         print('result',n1-n2)
#         break
#     if(c==3):
#         print('result',n1*n2)
#         break
#     if(c==4):
#         print('result',n1/n2)
#         break

# arr=[2,3,4,4,5,8,8,3,3,4,5,3,4]

# a=set(arr)
# print(a)
# for i in range(len(a)):
#     print(arr.count(a[i]))

# def name(*name):
#     print(name)
# name("darshan",'shubham','nishad','kharanshu')



# def personalInFo(first_name,last_name):


# text file and binary file we can acces using python using open()
# f =open('myfile.txt','w')
# print('name of file',f.name)
# print('file mode ',f.mode)
# print('readeble',f.readable())
# print('writeable',f.writable())
# print('file has close',f.closed)

# arr=[' darshan',' shubham',' nishad',' rohan',' mohan']
# f.writelines(arr)
# f.close()
# print('file has close',f.closed)
# import csv
# f =open('student.csv','a',newline="")
# a=csv.writer(f)
# # a.writerow(["rollno", "stdname","mobileno"])
# rollno=int(input())
# stdname=input()
# mobileno=int(input())
# a.writerow([rollno, stdname,mobileno])



# import csv

# def Enterdata(rollno, stdname,mobileno,age):
#     a.writerow([rollno, stdname,mobileno,age])

# def reitrive():

# f=open('darshan.csv','a',newline="")
# a=csv.writer(f)
# # a.writerow(["rollno", "stdname","mobileno","age"])
# print('1 . enter student data 2. read student record')
# n=int(input("enter your choice:--"))
# if(n==1):
#     rollno=int(input("roll no"))
#     stdname=input("stdname")
#     mobileno=int(input("mobileno"))
#     age=int(input("age"))
#     Enterdata( rollno, stdname,mobileno,age)

# a= int(input())
# b= int(input())
# try:
#     print(a/b)

# except (ValueError ,ZeroDivisionError) as mess:

#     print(mess)
# finally:
#     print('i will allways executrd')

# try:

#     a= int(input())
#     b= int(input())
#     try:
#         print(a/b)

#     except ZeroDivisionError as mess:
#         print(mess)
    
   
# except ValueError as mess:
#     print(mess)
# import csv
# f=open('darshan.csv','a',newline="")
# a=csv.writer(f)
# try:
#     rollno=int(input("roll no:--"))
#     stdname=str(input("stdname:--"))
    
#     mobileno=int(input("mobileno:--"))
        
    
        
#     age=int(input("age:--"))
# except ValueError as mess:
#     print(mess)
# a.writerow([rollno, stdname,mobileno,age])
# from sumof1standLast import n
# print(n)

# //////////////////////////

# salary=int(input("enter salary :--"))
# year=int(input("enter year of service :--"))
# if(year>5):
#     print(int(salary+salary*5/100))
# else:
#     print('not eligible for salary')
# /////////////////////


# length=int(input("enter length :--"))
# breadth=int(input("enter breadth :--"))
# if(length==breadth):
#     print("it's square")
# else:
#     print('not square')
# /////////////////////////////


# n1=int(input("enter 1st no:--"))
# n2=int(input("enter second no :--"))
# if(n1>n2):
#     print(n1,'is larger than',n2)
# elif(n1<n2):
#      print(n2,'is larger than',n1)
# else:
#     print(n2,'equal to',n1)

# //////////////////////////////////////////////////////////////////////////////


# n1=int(input("enter quantity:--"))
# if(n1<1000):
#     print('price:---',n1*100)
# else:
#     print('price:--' , (n1*100)-((n1*100*10)/100))

# ////////////////////////////////////////////////////////////////////
# marks=int(input("enter marks:--"))
# if(marks<25):
#     print('grade F')
# elif(45>=marks>25):
#     print('grade E')
# elif(50>=marks>45):
#     print('grade D')
# elif(60>=marks>50):
#     print('grade C')
# elif(80>=marks>60):
#     print('grade B')
# else:
#     print('grade A')

# //////////////////////////////////////////////////////////////////////


# age=list(map(int,input().split()))
# print("person",(age.index(max(age)))+1)
# print("person",(age.index(min(age)))+1)

# //////////////////////////////////////

# a=int(input())
# print(abs(a))
# ///////////////////////////////////////////

# 88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# classs and OOP
# class New:
#     x=10
#     def display(self):
#         print('hello world')

# a=New()
# a.display()
# print(a.x)

# python class have default constuctor
# constuctor assign memory to object
# constuctor exicute first
# if we call class constructor exicute autometicaly
# def __init__(self):
# thats why the we can call funcrion object outof class by refering the class beacause class have reference of all object and function

# class Newclass:
#     def __init__(self):
#         print('my name is constuctor and i always exicute first')
#         self.a='sonal'
#         self.age=12
#         self.id=101
#     def show(self):
#         print('hello world')
#         print('my name is  ',self.a)
#         print('my age is  ',self.age)

# a=Newclass()
# how many type of valiable we can declear in class




# class Student:
#     def __init__(self):
#         self.name='prashant'
#         self.age=32
#         self.rollno=21
#         self.branch:'cs'
#         self.mb:0000000000
# obj=Student()
# print(obj.__dict__)



# class Student:
#     def __init__(self):
#         self.name='prashant'
#         self.age=32
#         self.rollno=21
#         self.branch='cs'
        
#     def getdata(self):
#         self.mb=143495845732297332
# obj=Student()

# obj.getdata()
# # memory is not allocated to the mb unless and untill we call getdata fuction
# print(obj.__dict__)
# # instant variable are varialble added in constuctor after the creating class
# obj.last='chatrawat'
# print(obj.__dict__)

# # we and delete instance variable using del 
# del obj.name
# print(obj.__dict__)

# /////////////////////////////////////////////////////////////////////////////
# python does not support abstract calls we have to import from abs
# first we need to create a class by passing ABC and creat function by calling abstacmenthod
# than we can use as stander for each new class we creating


# from abc import ABC ,abstractmethod
# class Programing(ABC):
#     @abstractmethod
#     def traning(self):
#         pass
#     @abstractmethod
#     def placement(self):
#         pass
# class Ashish(Programing):
#     def traning(self):
#         print('c,c++,java')
#     def placement(self):
#         print('dsa traning')
# class Ankush(Programing):
#     def traning(self):
#         print('c,c++,java')
#     def placement(self):
#         print('dsa traning')
# class Prashant(Programing):
#     def traning(self):
#         print('c,c++,java')
#     def placement(self):
#         print('dsa traning')
# obj1=Prashant()
# obj1.traning()
# obj1=Ankush()
# obj1.traning()


# from abc import ABC, abstractmethod
# class IRCTC(ABC): #abstract class
#     @abstractmethod
#     def bookTicket(self): #abstract method
#         pass
# class MakeMyTrip(IRCTC):
#     def bookTicket(self):
#         print("    Welcome to MakeMYTrip")
#         source=input("Enter a source station name")
#         destination=input("Enter destination name")
#         date=input("Enter date")
# class goIBIBO(IRCTC):
#     def bookTicket(self):
#         print("    Welcoe to goIBIBO")
#         source=input("Enter a source station name")
#         destination=input("Enter destination name")
#         date=input("Enter date")
# class Yatra(IRCTC):
#     def bookTicket(self):
#         print("    Welcome to Yatra")
#         source=input("Enter a source station name")
#         destination=input("Enter destination name")
#         date=input("Enter date")  
# m=MakeMyTrip()
# m.bookTicket()

# g=goIBIBO()
# g.bookTicket()

# y=Yatra()
# y.bookTicket()


# class Base:
#     def _init_(self):
#         print("Parent class constructor")
#         self.a = "TCET"
#         self.c = "DJSCE"
# class Derived(Base):
#     def _init_(self):
        
#         Base._init_(self)
#         print("Calling private member of base class")
        
        
# obj1 = Derived()
# print(obj1.a)


# n=int(input())
# def note(n):
#     th=n//1000 
#     a=n-1000*th
#     H=a//100
#     b=a-100*H
#     t=b//50
#     c=b-50*t
    
      
#     print(th,H,t,c)
# note(n)
# num=list(map(int,input().split()))
# n=int(input())
# # num=list(map(int,input().split()))

# count=0
# for i in range(len(num)):
#     if(num[i]==n):
#         count+=1
# print(count)

for i in range(1,)




        













