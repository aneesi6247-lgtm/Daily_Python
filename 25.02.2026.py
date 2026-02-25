# match command
color = input("Please Enter the color : ")
match color:
    case "Green":
        print("you can go")
    case "Red":
        print("You cant go")
    case "Yellow":
        print("watch out")
    case _:
        print("the light is broken")

# count the number of particular word in any pharase#

word = "Artificial Intelligence"
count = 0
for ch in word:
    if (ch == "e"):
        count+=1
print (count)
# create a program to count the sum of n natural numbers

n = 5
sum = 0
for val in range(1,n+1):
    sum += val
print(sum)


# get the factorial of any number

def fac(n): 
    fac= 1
    for val in range(1,n+1):
        fac *= val
    print(fac)
fac(5)

# print the digits of any numbers
n = 354
first = n % 10
print(first)
n = n//10
sec = n % 10
print(sec)
n= n//10
print(n)
