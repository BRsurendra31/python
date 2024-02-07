##conditional statement -

#IF-ELSE  :
'''
if condition :
    #statement
else :
    #statement 

'''

'''
#e.g take an integer and tell whether it is +ve or -ve 

number= int(input())
if number >=0 :
    print("number is +ve ")
else :
    print("number is -ve ")

#op 
#5
#number is +ve
#-2
#number is -ve
    
'''

'''
#e.g 2 take a number and tell wheethre it is even or odd 

number = int(input())

if number % 2 ==0 :
    print("number is even") # 6, even
else :
    print("number is odd") #7, odd
'''

# Elif : else if 

'''
cp = int(input("Enter cost price : "))
sp = int(input("Enter selling price : "))

if cp < sp:
    profit = sp - cp
    print("ptofit =" , profit)
elif cp > sp :
    loss = cp - sp 
    print("loss =",loss)
else :
    print("no profit no loss")

# Enter cost price : 400
# Enter selling price : 600
# ptofit = 200
'''

# use of and , or operators  : 
'''
eng_marks = int(input("ENGLISH : "))
math_marks = int(input("MATH  : "))

if eng_marks > 80  and math_marks > 80 :
    print(" Grade A ")
elif eng_marks > 80 or math_marks > 80 :
    print("Grade B")

else :
    print("Grade C")

'''

'''
# Nested IF-ELSE :

n1 = int(input("n1 :"))
n2 = int(input("n2 :"))
n3 = int(input("n3 :"))

if n1 > n2 :
    if n1 > n3 :
        print(n1, "is greatest")
    else :
        print(n3, "is greatest")
else :
    print(n2 , "is greatest")

'''

'''

#MATCH case 
    # removes multiple ef else statement

#e.g Design calcuator 

num1 = int(input("Enter first no. :"))
num2 = int(input("Enter second no. :"))

opetator = input("Enter operator :")

match opetator :
    case "+" :
        print("sum is :", num1 + num2)
    case "-" :
        print("sum is :", num1- num2)
    case "*" :
        print("sum is :", num1 * num2)
    case "/" :
        print("sum is :", num1 / num2)
    case _ :
        print("Enter a valid operator :")

#op
# Enter first no. :2
# Enter second no. :3
# Enter operator :*
# sum is : 6

# Enter first no. :3
# Enter second no. :5
# Enter operator :&
# Enter a valid operator :

'''

'''
#Ternary operator 
    #removes multiline if else in single line

# umbrella = "lana h" if raining else "no"

#e.g - find even or odd 

num = int(input())
output = "even" if num % 2 ==0 else "odd"
print(output)
    
# 4
# even 
# 3
# odd 

'''

