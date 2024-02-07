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
n = int(input())
for i in range(n): # loop for row 
    for j in range(1, n+1): # loop for loc
        print(j, end= "") # end is for printing j in single line till loop terminate
    print() # for next line


    


