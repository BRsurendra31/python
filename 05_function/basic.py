## Function :

# Block of ewusable code that performs a specific task

# Types of function 

    #1. Built-in func :
        # print()
        # sum()
        # append() etc

    #2. user defined func :
        # > defined by user 


## User defined function :

'''
    def func_name (parameters ):
        #statement
        return expression

'''

#printHello() we cannot call a func before its definition
def printHello():
    print("Hello")

printHello() #Hello

#eg1 sum of two numbers -

def sum(a,b):
    print("a", a)
    print("b", b)
    ans = a + b
    return ans

#1. positional arguments 
print("sum is :" ,sum(2,4)) #sum is : 6

# a 2
# b 4
# sum is : 6



def add(n1, n2):
    print("n1", n1)
    print("n2", n2)
    ans = n1 + n2
    return ans

#2.keyword argument 
print("the sum is :", add(n2=3, n1=5)) # keywords matters not position

# n1 5
# n2 3
# the sum is : 8


#3 default argument 
    # > takes default paramenter in operation 
def add1(n1, n2=0):
    print("n1", n1)
    print("n2", n2)
    ans = n1 + n2
    return ans

print("the sum is :", add1(3))

# n1 3
# n2 0
# the sum is : 3


# 4. Arbitrary arguments (variable legth arguments *args and **kwargs -> this *args work as Tuple, and **kwarg work as dictionary )

    #4.1 *args -
def addNumbers( *args):
    sum =0
    for i in args:
        sum +=i
    return sum

output1 =addNumbers(2,3,5,6)
output2 =addNumbers(10,34,67)

print("the sum1 is  :" , output1, " the sum2 is :", output2)
# the sum1 is  : 16  the sum2 is : 111

# 4.2 **kwargs - keyworded args 

def studInfo( **kwargs):
   for x,y in kwargs.items():
       print(x, " :", y)



studInfo(name="surendra", age="22", city="Delhi")
studInfo(name="raj", age="23", city="Bangluru")

# name  : surendra
# age  : 22
# city  : Delhi
# name  : raj
# age  : 23
# city  : Bangluru




## Nested func :

def outer_func():
    x=1

    def inner_func():
        y=2
        result = x +y
        return result
    return inner_func()

output = outer_func()
print(output) #3


## Pass by value and pass by reference 

#1 Pass by value :
'''
    >Its for Immutable objects - strings, integers, floats, tuples
    >whe we passed an object to a function , a coppy of obj is created and assign to local variable in a function
    >
    > any change made to them inside a function , do not effect the original variable outside func 
'''

def add1(x):
    x = x +1
    print("x inside function :", x)
    return x

x=5
print( "result :",add1(x))
print("x outside func :", x)

# x inside function : 6
# result : 6
# x outside func : 5



#2 Pass by reference :

'''
    > we paass Mutable objects - list, dictionary
    > reference to actual obj is passed 
    > chang made anywhere effects original object

'''

def modifyList(lst):
    lst.append(4)
    print("Inside func list :", lst)


lst = [1,2,3]
modifyList(lst)
print("outside func list :", lst)

# Inside func list : [1, 2, 3, 4]
# outside func list : [1, 2, 3, 4]


#qsn calculate factorial :

def factorial(n):
    ans = 1
    if n==0:
        ans=1
    else :
        for i in range(1, n+1):
            ans *=i
    return ans 

n= int(input("Enter numbers :"))
print("the factorial of ", n, "is :",factorial(n))
    
# Enter numbers :5
# the factorial of  5 is : 120