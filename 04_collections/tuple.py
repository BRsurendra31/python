## Tuple :

# sequence datatype

'''
                0        1        2
>e.g colors =("blue", "green", "orange")
                -3         -2       -1
>Immutable - we cannot update 
>Duplicates allowed 
>Any data types 
>Mix of diffrent datatypes 
'''

# creating tuple 
colors = ("red", "green", "blue")
fruit = tuple(("apple", "banana"))

 #creating tuple with 1 item 
fruit = ("apple",) # comma is compulsory otherwise it is treated as string variable 
print(type(fruit))  #<class 'tuple'>
fruit = ("apple")
print(type(fruit)) #<class 'str'>


#Length of tuple 
print(len(colors)) #3


# Accessing tuples
    # same as list
tuple1 = (10,20, 30, 40)
print(tuple1[0]) #10
print(tuple1[3]) #40
print(tuple1[-2]) #30
print(tuple1[0:2]) #(10, 20) #+ve range indeding - Left to Right acces by compiler
print(tuple1[-2:]) #(30, 40) #-ve range indexing - also Left to Right accees by compiler e.g -3 , -2 , then -1  


#check if an item exists in tuple

'''
num1 = int(input("Enter num1 :"))
if num1 in tuple1 :
    print(num1," present in tuple")

else :
    print(num1 ," not present in tuple")

# Enter num1 :10
# 10  present in tuple
# Enter num1 :23
# 23 not  present in tuple
    '''

# ## Traverse in tuple :
    
# for i in tuple1 :
#     print(i, end=" ") #10 20 30 40



##cancatenate 2 tuples :
    
tuple2 = ("apple", "mango", "banana")
print(tuple1 + tuple2) #(10, 20, 30, 40, 'apple', 'mango', 'banana')


##Unpacking a tuple :

t1, t2, t3 =tuple2
print(t1, t2, t3) #apple mango banana




## Tuple vs List 
'''
    >Iterating through a tuple is faster than list
    >List are mutable whereas 'Tuples' are immutable 
    >Tuples that contain immutable elements can be used as key for dictionary
'''


## Reverse a tuple :

tpl = (12, 13,56,67,78,90)
list =[]

# adding reversed values in list 
for x in reversed(tpl) :
    #print(x, end=" ") # this will give reversed values not reversed tuple 
    list.append(x)  #this proces give you reversed tuple

output_tuple = tuple(list) # typecast into tuple 
print(output_tuple) #(90, 78, 67, 56, 13, 12)

