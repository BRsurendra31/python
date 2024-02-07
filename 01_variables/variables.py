print("Namaste world")


#string 
name = "Surendra"

#Integer
roll_no = 12

#Float
percentage = 87.8

#Boolean
is_student = True

print(name ,"\n" ,roll_no,"\n" , percentage,"\n" , is_student)

# can update with same variable name 
percentage = 70.5
print(name ,"\n" ,roll_no,"\n" , percentage,"\n" , is_student)

#type 

print(type(percentage)) # <class 'float'>

# print 
# print("my name is "+ name + "my roll no. is "+roll_no + ) #error-bcz we cannot concatenate two different types directly
print("my name is "+ name + " my roll no. is ",roll_no  ); #my name is Surendra my roll no. is  12

#printing with expresions 
print("my percentage has changed to ",percentage-1.0)  #my percentage has changed to  69.5

#printing with separators
print(name,roll_no, percentage, sep="-" )#my percentage has changed to  69.5

x=1
y=2
z=3
print(x,y,z, sep="->") #1->2->3