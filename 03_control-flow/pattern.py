'''
#1. print sqare patern of *
******
******
******

'''
# n = int(input("enter n")) 
# for _ in range(n):
#     print("*" *5) // 5 represent col


#2. print given pattern
'''
for n=4

1234
1234
1234
1234

for n=6
123456
123456
123456
123456
123456
123456

'''
# n = int(input())
# for i in range(n): # loop for row 
#     for j in range(1, n+1): # loop for loc
#         print(j, end= "") # end is for printing j in single line till loop terminate
#     print() # for next line



#3 Print given pattern 
    # 1
    # 12
    # 123
    # 1234


# n =int(input("Enter n :"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()
    


# print given pattern :
'''   
       
       1
      123
     12345
    1234567
''' 
n = int(input("Enter n :"))
for i in range(1, n+1): #loop for rows
    print(" "*(n-i), end="") # printing spaces
    for j in range(1, 2*i):
        print(j, end="") #printing digits
    print()



    


