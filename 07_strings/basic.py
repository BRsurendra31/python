## string 
# it is a sequence of characters
# it can be created using 
    #single quote : 'Hello world'
    #double quote : "Hello world"
    #Triple quote also: '''Hello world'''

# string is Imutable 
    # but we can create new string by manipulating origional string

name1 ='surendra'
name2 ="kumar"
name3 ='''chauhan'''

print(name1,name2, name3) #surendra kumar chauhan


## creating multiline string 
    # can do it by tripple quotes ''''''

msg = '''
        Hi
        This is a mail
        regarding ypour previous 
        performance in  xyz comapany
        '''
print(msg)
print(len(msg)) #114

# Hi
# This is a mail
# regarding ypour previous
# performance in  xyz comapany

# indexing in string :
    # >same as array(list) i.e 0 to n-1

text = "Hello, world!" # space counted as character 
print(text[0]) #H
print(text[5]) #,
print(text[7])#w 
print(text[1 :4])#ell

# -ve indexing also allowed 
print(text[-1])
print(text[-1:-3]) #!, bcz it work left to right 
print(text[-3 :-1]) #ld


# Traversing a string 
text2 = "Hello"
for i in text2 :
    print(i)

# H
# e
# l
# l
# o
    
# find char/substring in a string 
print(text2.find("l")) #2, find() returns indx of 1st occurence of character
print(text2.find("z")) #-1, mean not found 
print(text2.find("o")) #4


##operations :
    # > all operations returns totally a new string , no any efect of original bcz its immutable properties 
# Slice 

name = "RajShekhar"
print(name[2:5]) #jSh
print(name[:4]) #RajS, returns from 0 to n-1
print(name[2:]) #jShekhar, returns from 2 to n-1

## Modigy 

# to upper case 
str1 = "surendra"
str2 = str1.upper()
print(str2) #SURENDRA

# to lower case 
str3 = str2.lower()
print(str3) #surendra

# caitalizing 1st char of string 

str4 = str3.capitalize()
print(str4) #Surendra

# stripping / removing trailing white spaces 

str1 = "    Hello world     "
print(str1.strip()) #Hello world

# replace 
    # str.replace("substring", "newsubstring", count)

str1 = "Hello world, what a beautiful world it is !"
print(str1.replace("world", "earth")) #Hello earth, what a beautiful earth it is !  ,replace all accurences 
print(str1.replace("world", "earth", 1)) #Hello earth, what a beautiful world it is !  ,replace 1st accurences as per count


# split :
    # split the string into list of substrings 
    # str.split(sep, maxsplit) # separator
str = "apple banana mango "
res= str.split() #splits by default using separator as white space 
print(res) #['apple', 'banana', 'mango']

string2= "my, name, is ,surendra "
result = string2.split(" ,", 2)
print(result) #['my,', 'name,', 'is ,surendra ']

# cancatenation :

s1 = "surendarn "
s2 = "kumar"
print(s1 + s2) #surendarn kumar


#  formating :

student_name = "surendra"
marks = 98

detail= "The student name is {s}, and marks is {m}".format(s=student_name, m=marks) # {} > called placeholder that takes variable 
print(detail) # The student name is surendra, and marks is 98









