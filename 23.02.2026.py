# For Today
# write a program to swap the values of two integers without introducing third one. 
a = 5
b = 3
a = a+b
b= a - b
a = a - b
print("a=:", a)
print("b=:", b)

# take a number from the user and print its int and floating part seperately. 

num = float(input("Please enter a floating number"))
int_part = int(num)
float_part = num - int_part
print("the int part is: ", int_part)
print("The float part is: ", float_part)
