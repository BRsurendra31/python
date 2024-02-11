## OOPS :

# Classes :
'''
    > user defined datatypes 
    > blueprints/templates for an object
'''

#Object :

    # >intance of class
    # >mimic real world entyties 


class Student :
    # method
    def set_name(self,name):
        self.name = name 
    
    def get_name(self):
        return self.name
    
#obj creation 
stu1 = Student()
stu1.set_name("surendar")
print(stu1.name) #surendar
print(stu1.get_name()) #surendar, bcz stu1 goes as a parameter to get_name ()

stu2 = Student()
stu2.set_name("raj")
print(stu2.get_name()) #raj


#qsn1

class Rectangle:
    def set_dimensions(self, height, width):
        self.ht = height
        self.wdth = width
    
    def area (self):
        return self.ht * self.wdth
    
    def perimeter(self):
        return  2*(self.ht + self.wdth)
    

rectangle1 = Rectangle()
rectangle1.set_dimensions(4,3)
print(rectangle1.area()) #12
print(rectangle1.perimeter()) #14


# Constructor :
    # >special func that get invoked everytime an obj is created 
    #def __init__(self, parameter1, parameter2,...) :
        #initialize instance variable(attributes )
 
class Rectangle:
    # constructor
    def __init__(self, height, width):
        print(f"a rectangle is created with height {height}, and width {width}") # f is compulsory for placeholder use 
        self.ht = height
        self.wdth = width
    
    def area (self):
        return self.ht * self.wdth
    
    def perimeter(self):
        return  2*(self.ht + self.wdth)
    
rectangle1 = Rectangle(10,20)
print(rectangle1.area()) #200
print(rectangle1.perimeter()) #60


##Attributes :

# class attribute :
    # >attributes defined inside class 
    # > all obj instances will have these attributes 

# Instance attribute :

    # > specific to a particular instance / obj

class Rectangle:
    # attribues 
    def __init__(self, height, width):
        print(f"a rectangle is created with height {height}, and width {width}") # f is compulsory for placeholder use 
        self.ht = height # data attributes 
        self.wdth = width
    
    def area (self): # ,method attribute
        return self.ht * self.wdth
    
    def perimeter(self):
        return  2*(self.ht + self.wdth)
    
rectangle1 = Rectangle(10,20)
print(rectangle1.area()) #200
print(rectangle1.perimeter()) #60

rectangle1.angle = 90 # instance attribute 
print(rectangle1.angle) #90



## Access modifiers :

# public modifiers : 
    # > by default class attributes are public 

# class ABC :
#     def __init__(self):
#         self.public_attribute=non # public attributes 

#     def punblic_function(): #public func
#         pass


#private 
    # >cannot access outside its block
# class ABC :
#     def __init__(self):
#         self.__private_attribute=10 # private attribute

#     def __private_function():
#         pass

# obj1 = ABC()
# print(obj1.__private_attribute) #obj error 
# print(obj1.__private_function())# obj error

# protected
    # >accessible within class and its outside subclass 

# class ABC :
#     def __init__(self):
#         self._protected_attribute=10

#     def _protected_function():
#         pass 



# obj2=ABC()
# print(obj2._protected_attribute) # error 



## oops concepts :

#1 Inheritance :

class Parent:
    def __init__(self):
        self.super_attribute=True
        print("This is parent class")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is child class")
        print(self.super_attribute) #True

child1 =Child()