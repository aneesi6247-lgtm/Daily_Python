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

# write a function to return the number of digits of a number
num = "23423423"
cnt=0
for val in num:
    cnt+=1
print(cnt)

# write a programe to get all the numbers in between 1 to 100 which are divisible by 3 and 5

for k in range(1,101,1):
    if(k%3==0 and k%5==0):
        print(k)
# write a programe to continously get an input from the user and decide weather input is positive or negative and stop it only when the user write "Quite"
 
while True:
    inp = (input("Please enter a number:"))
    if (inp=="quite"):
        break
    try:
        inp1 = int(inp)
        if (inp1>0):
            print(" the value is positive")
        elif inp1<0:
            print("the number is negative")
        else:
            print("the number is zero")
    except ValueError:
            print("please enter a valid number or quite")

# make a calculator

def cal(a,b, operation):
    if operation =="+":
        print(a+b)
    if operation =="-":
        print(a-b)
    if operation =="*":
        print(a*b)

cal(13,532,"+")

#write a program to tell weather the number is prime or not

get = int(input("Please enter the number:"))
if get <1:
    print("not a prime number")

for val in range (2,get):
    if get%val == 0:
        print("not a prime number")
        break
    else:
        print("IS PRIME NUMBER")
        break
# write a code to print all the prime numbers from 1 to 100

n = 100
for val in range (2,n+1):
    is_prime = True
    for i in range(2,val):
        if val % i == 0:
            is_prime= False
            break
    if (is_prime):
        print(val)
