
#In Python, classes and objects are fundamental concepts in object-oriented programming (OOP).

#Class
#A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Think of a class as a template or a prototype.

#example of a class in Python:

class ClassName:
    # class definition 
#Here, we have created a class named ClassName.

#Let's see an example,

 class Bike:
    name = ""
    gear = 0

#Bike - the name of the class
#name/gear - variables inside the class with default values "" and 0 respectively.
#Note: The variables inside a class are called attributes.


#Python Objects
#An object is called an instance of a class.

##Suppose Bike is a class then we can create objects like bike1, bike2, etc from the class.

#Here's the syntax to create an object.

objectName = ClassName()
#Let's see an example,

# create class
class Bike:
    name = ""
    gear = 0

# create objects of class
bike1 = Bike()
#Here, bike1 is the object of the class. Now, we can use this object to access the class attributes.



#to print even no using fn mthd
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
def even(a):
    for value in a:
        if value%2==0:
            list2.append(value)
    return list2
even(list1)
 
#to print even and odd no using fn mthd   
list1=[1,2,3,4,5,6,7,8,9,10]
def even(a):
    list2=[]
    list3=[]
    for value in a:
        if value%2==0:
            list2.append(value)
        else:
            list3.append(value)
    return list2,list3
a=even(list1)
a[1]


#CLASS

class Demo:
    def even(self):
        a=[1,2,3,4,5,6,7,8,9,10]
        list2=[]
        list3=[]
        for value in a:
            if value%2==0:
                list2.append(value)
            else:
                list3.append(value)
        return list2,list3
    def shafna(self):
        a=89
        b=78
        return(a+b)
    def square(self):
        c=10
        return c**2
m=Demo()
m
type(m)
dir(m)
m.even()
m.shafna()
m.square()





class Star:
    def __init__(self,num):
        self.num=num
    def shafna(self):
        for i in range(self.num):
            print('*'*(i+1))
d=Star(4)
d
d.shafna()



class Even:
    def __init__(self,num):
        self.num=num
    def shafna(self):
        b=[]
        for value in self.num:
            if value%2==0:
                b.append(value)
        return b
a=[1,2,3,4,5,6,7,8,9,10]
r=Even(a)
r.shafna()




# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values

bike1.name = "Mountain Bike"
bike1.gear = 11

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")



#The __init__() Function
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

#?Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)




#TO FIND SUM 


list1=[1000,2000]
sum=0
for variable in list1:
    sum=sum+variable
print(sum)
def shafna(a):
    sum=0
    for variable in a:
        sum=sum+variable
    return sum   
shafna(list1)



class Value:
    def __init__(self,a):
        self.a=a
        
    def shafna(self):
        sum=0
        for variable in self.a:
            sum=sum+variable
        return sum
list1=[1,5,9,6,4,9,3]
b=Value(list1)
b.shafna()



#TO FIND SUM USING WHILE LOOP
class Value1:
    def __init__(self,a):
        self.a=a
        
    def shafna(self):
        sum=0
        index=0
        while index<len(self.a):
            sum=sum+self.a[index]
            index=index+1
        return sum
c=Value1(list1)
c.shafna()



#EVEN ODD USING WHILE LOOP
class Even:
    def __init__(self,num):
        self.num=num
    def shafna(self):
        sum=0
        while sum<=20:
            sum=sum+1
            if sum%2==0:
                print(sum)
        while sum>=1:
            sum=sum-1
            if sum%2==1:
                print (sum)
a=[1,2,3,4,5,6,7,8,9,10]
r=Even(a)
r.shafna()


