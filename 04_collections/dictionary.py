
## Dictionary :

# sequence datatypes 
# stores key value pairs 
# properties :
'''
    >ordered 
    >Changeable 
    >Unindexed 
    >Duplicates not allowed
    >any datatype

numbers = {
    "ram" : 5462132134,
    "shyam": 235467898,
    "gita" : 325467689
}     keys      values

'''

# creating dictionary :

numbers = {
    "ram" : 5462132134,
    "shyam": 235467898,
    "gita" : 325467689
}  

print(numbers) #{'ram': 5462132134, 'shyam': 235467898, 'gita': 325467689}

# access item 
print(numbers["ram"]) #5462132134
print(numbers.get("ram")) #5462132134

# print all keys 
print(numbers.keys()) #dict_keys(['ram', 'shyam', 'gita'])

#printing all values 
print(numbers.values()) #dict_values([5462132134, 235467898, 325467689])



# update value 

numbers["ram"] = 2222222
print(numbers) #{'ram': 2222222, 'shyam': 235467898, 'gita': 325467689}

# add new pairs 

numbers["raju"] = 2345
print(numbers) #{'ram': 2222222, 'shyam': 235467898, 'gita': 325467689, 'raju': 2345}



## add another dict into one 

more_numbers = {
    "surya" : 2345,
    "maya"  : 2354,
    "sarita" : 2345
}

numbers.update(more_numbers)
print(numbers) #{'ram': 2222222, 'shyam': 235467898, 'gita': 325467689, 'raju': 2345, 'surya': 2345, 'maya': 2354, 'sarita': 2345}


# remove element 

numbers.pop("ram")
print(numbers) #{'shyam': 235467898, 'gita': 325467689, 'raju': 2345, 'surya': 2345, 'maya': 2354, 'sarita': 2345}

numbers.popitem() # removes last item , {'shyam': 235467898, 'gita': 325467689, 'raju': 2345, 'surya': 2345, 'maya': 2354, 'sarita': 2345}


numbers.clear() # this will empty the dictionary 
#print(numbers) #{}



# printing keys of dict

dict ={
    "surya" : 2345,
    "maya"  : 2354,
    "sarita" : 2345
}

for x in dict :
    print(x)

# surya
# maya
# sarita
    
# print values 
    
for x in dict :
    print(dict[x])

# 2345
# 2354
# 2345
    
## print pairs 
    

for x in dict.items() :
    print(x)


# ('surya', 2345)
# ('maya', 2354)
# ('sarita', 2345)


for x,y in dict.items() :
    print(x,y)

# surya 2345
# maya 2354
# sarita 2345
    


# nested dictionary 
    
dict1 ={
    "Area1" :{
        "surya" : 2345,
    "maya"  : 2354,
    "sarita" : 2345
    },
    "Area2" : {
        "ram" : 5462132134,
    "shyam": 235467898,
    "gita" : 325467689
    }
}

print(dict1["Area1"]["surya"]) #2345


# sum of all values of dictionary 

dict ={
    "x" : 10,
    "y" : 20,
    "z" :30
}

print("sum of all values is :", sum(dict.values())) #sum of all values is : 60



## List into dictionary :
    # >given two lists l1 l2 
    # >l1 represent keys and l2 values 

l1 =["a", "b", "c", "d"]
l2 =[10,20,30,40]

dict_from_list =dict(zip(l1,l2))
print(dict_from_list) #{'a': 10, 'b': 20, 'c': 30, 'd': 40}