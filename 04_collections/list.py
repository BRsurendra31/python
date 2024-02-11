##colletions(Arrays)
# 1. list
# 2. tuple
# 3. set
# 4. dictionary


##1list :
# Sequence datatype 
#allows us to store multiple items in a single variable
#properties :
    # indexed (0 to n-1)
    # ordered
    # mutable
    # Duplicates allowed 
    # any datatypes 
    # mix of different data types

fruits =["apple", "banana", "mango", "orange"]
# print(fruits)
# print(type(fruits))
# print(len(fruits))

# #op
# ['apple', 'banana', 'mango', 'orange']
# <class 'list'>
# 4

#checking if an item present in the list 
# if "banana" in fruits:
#     print("banana is present in the list")
# if "tomoto" not in fruits:
#     print("tomoto is not in the list") 

# # banana is present in the list
# # tomoto is not in the list

#Accessing items of list :
'''
    1. indexing(+ve/-ve indexing) :
                0   1   2  3
        list =[10, 12, 34,67]
               -4  -3 -2  -1
    2. Range of index (-ve/+ve):
        list[start indx : end indx] # end indx exlusive
        e.g list[1 : 3] gives list[ 12 , 34]
            list[-3, -1] give same [12, 34]
'''

print(fruits[1]) #banana
print(fruits[-1]) #orange
print(fruits[1: 3]) #['banana', 'mango']
print(fruits[-4 : -2]) #['apple', 'banana']


#Adding element to the list :
'''
    1. append() :-
        adds item to end of list
    2. insert() :-
        inserts an item on a particular indx 
    3. extend() :-
        adds other list into existing list 
'''

list1 = [10, 20, 30 , 40]
list1.append(47)
print(list1) #[10, 20, 30, 40, 47]
list1.insert(2, 34)
print(list1) #[10, 20, 34, 30, 40, 47]

list2 = [23, 45,66,78]
list1.extend(list2)
print(list1) #[10, 20, 34, 30, 40, 47, 23, 45, 66, 78]


#Remove element from list :
'''
    1. remove() :-
        it removes specified item 
    2. pop() :-
        it removes item at given indx or else removes last item
'''

numList = [23,45,6,89,80]
numList.remove(45)
print(numList) #[23, 6, 89, 80]
numList.pop(2) # remove at indx 2
print(numList) #[23, 6, 80]
numList.pop() 
print(numList) #[23, 6] last item get removed 


#Change item in list :
# 1. at an Index
# 2. in a range 

mixList = [23,45, "banana", "tomoto", 3.5]
print(mixList) #[23, 45, 'banana', 'tomoto', 3.5]

mixList[2] = "potato"
print(mixList) #[23, 45, 'potato', 'tomoto', 3.5]

mixList[1 :3] =[90, "bagan"]
print(mixList) #[23, 90, 'bagan', 'tomoto', 3.5]



## sorting a list 
    # 1. ascending order (by default)
    # 2. descending order

# mixList.sort()
# print(mixList) # Error- we cant sort distinc types

nameList = ["surendra", "mohan", "rajan", "suraj", "arun"]
nameList.sort()
print(nameList) #['arun', 'mohan', 'rajan', 'suraj', 'surendra']

numList3 = [3,6,8,1,8,9,4,4]
numList3.sort(reverse=True) # reverse sort
print(numList3) #[9, 8, 8, 6, 4, 4, 3, 1]


## Reverse the list
numList3.reverse()
print(numList3) #[1, 3, 4, 4, 6, 8, 8, 9]


##List comprehension :

'''
when we want to make new list from item of an existing list
e.g list =[34,70,12,34,85,30]
 want to make new list whose item is less than 45
i.e [34,12,34,30]
'''
# traditional way 
lst = [34,70,12,34,85,30]
newlst =[]
for i in lst:
    if i < 45 :
        newlst.append(i)
    
print(newlst) #[34, 12, 34, 30]

#By list comprehension :

newlst2 = [i for i in lst if i <45]
print(newlst2) #[34, 12, 34, 30]

##copy a list :

newlst2 = lst.copy()
print(newlst2) #[34, 70, 12, 34, 85, 30]

##cancatenate 

newlst2 = lst + newlst2
print(newlst2) #[34, 70, 12, 34, 85, 30, 34, 70, 12, 34, 85, 30]


## Nested list :
'''
             0  1    2     3
    list = [10,20,[30,40], 50]
                    0  1
    list[2] = [30,40]
    list[2][0] = 30
    list[2][1] = 40
'''

nums = [10,20,[30,40], 50,60]
print(nums[2]) #[30, 40]
print(nums[2][0]) #30
print(nums[2][1]) #40

nums.insert(4, [45,76])
print(nums) #[10, 20, [30, 40], 50, [45, 76], 60]
nums.append([23,45])
print(nums) #[10, 20, [30, 40], 50, [45, 76], 60, [23, 45]]


## swap in list 

n = int(input("Enter size of list :"))

list = []
print("Enter elements of list :")
for _ in range(n) :

    num = int(input())
    list.append(num)

print( "list before swaop :",list) 
indx1 = int(input("Enter indx1 :"))
indx2 = int(input("Enter indx2 :"))

#swaping 
temp = list[indx1]
list[indx1] = list[indx2]
list[indx2] = temp

print( "list after swap :",list)

# Enter size of list :5
# Enter elements of list :
# 10   
# 20
# 30
# 40
# 50
#list before swaop : [10, 20, 30, 40, 50]
# Enter indx1 :0
# Enter indx2 :4
#list after swap : [50, 20, 30, 40, 10]



