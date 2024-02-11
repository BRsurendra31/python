## Sets :
# sequence datatype
# container for storing multiple values in a variable
# set1 ={"ram", "sita", 4, 56.2}
# Properties :
'''
    > Unordered 
    > Immutable - cannot update existing items , but can rempve , add item
    > Unindexed 
    >Duplicates not allowed 
    >any dtatypes 
    > Mix of different Data types 
'''

# Creating  set 
names = {"ram", "sita", "gita", "aman", "babita"}
print(names) #{'babita', 'aman', 'ram', 'sita', 'gita'}

# length
print(len(names)) #5

# Accessing items 

for x in names :
    print(x ,end=" ") #babita aman gita ram sita

print()
## add element 

names.add("surendra")
print(names) #{'aman', 'gita', 'babita', 'sita', 'ram', 'surendra'} 

# Add another sequence i  a set 

name_list = ["saroj", "mohan"]
names.update(name_list)
print(names) #'sita', 'gita', 'surendra', 'ram', 'mohan', 'aman', 'babita', 'saroj'}

## Remove element 

names.remove("saroj") 
print(names) #{'mohan', 'surendra', 'sita', 'aman', 'babita', 'gita', 'ram'}

#names.remove("kanchan")
#print(names) #  errror- bzc kanchan is not in set
names.discard("mohan") # it also remove element but if element not present then it not throw any errror
print(names)



# Join 2 sets 

s1 = {'a','b','c'}
s2 = {'d', 'a', 'e'}

#print(s1 + s2) # + opereator not work for set

#method 1
print(s1, s2) #{'a', 'b', 'c'} {'d', 'e', 'a'}
print(s1.union(s2)) #{'a', 'b', 'd', 'e', 'c'}, duplicate is removed 

#method 2

s1.update(s2) # s2 ko s1 me add kar do
print(s1)  #{'d', 'e', 'c', 'b', 'a'}


#Qsn you have given 3 lists , you have to return commo element in form of list from all three using set 

l1 = [2,4,5,6]
l2 =[3,4,4,7]
l3 =[9,5,4,6,8]

#typecasting into set 
s1 =set(l1)
s2 =set(l2)
s3 =set(l3)

# apply intersection

s1s2 = s1.intersection(s2)
final = s1s2.intersection(s3)
print(list(final)) #[4]



