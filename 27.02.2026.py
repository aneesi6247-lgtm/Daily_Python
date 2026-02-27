# given a list of tuples with the info (name, subject):
# list all unique courses

list = [("anees", "math"), ("hamza", "english"), ("anees","phy"), ("hamza","english")]
new_set = set()
for name,course in list:
    new_set.add(course)

print(new_set)

# create dictionery student(name, set of courses)
student = {}
for name, course in list:
    if student.get(name)==None:
        student.update({name :set()})
        student[name].add(course)
    else:
        student[name].add(course)

print(student)

# get a string from the user and check weather it is Palindrome or not for example racecar
a = "Hello"
list2 = []
for val in a:
    list2.append(val)
print(list2)
list3=list2.copy()
list3.reverse()
print(list3)
if list3 == list2:
    print(f"the string {a} is palindrome")
else:
    print("the string is not a palindorme")

# merge two lists 

lis = [2,35,6434,3462345,13453445,3145,435,345,353]
lis1 = [3423,345,1345,345,1345,34,324,134,5]
print(lis+lis1)
lis2 = lis + lis1
lis2.sort()
print(lis2)

# given a tuple of all the integers value make two more with odd and even numbers

tup = (12,42,23,52,23,523,5,23,5,23,23,5,23,35,235,35)
tup1 =()
tup2=()
for val in tup:
    if val%2==0:
        tup1 = tup1 +(val,)
    if val%2!=0:
        tup2 = tup2 +(val,)
print(tup1)
print(tup2)

# Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
# depending on the operation they want to perform on the dictionary:
# A
# 1. - Add a student
# B
# 2. - Update marks
# 3. C
# - Search for a student
# 4. D
# - Display all students and marks

students = {
    "anees": 23,
    "hamza": 34,
    "hassan": 45
}

while True:
    print("\nMENU")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")

    choice = input("Enter your choice (A-E): ").lower()

    # A - Add student
    if choice == "a":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # B - Update marks
    elif choice == "b":
        name = input("Enter student name to update: ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # C - Search student
    elif choice == "c":
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} has {students[name]} marks.")
        else:
            print("Student not found!")

    # D - Display all
    elif choice == "d":
        print("All Students:")
        for name, marks in students.items():
            print(name, ":", marks)

    # Exit
    elif choice == "e":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")

# Given a list of words:
# words = ["apple","banana","kiwi","cherry","mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5,"banana": 6,"kiwi": 4,}
dic1 = {}
count = 0
words = ["apple","banana","kiwi","cherry","mango"]
for val in words:
    for k in val:
        count +=1
    dic1.update({val:count})
    count = 0
print(dic1)
# another simple way
words = ["apple","banana","kiwi","cherry","mango"]

dic1 = {}

for word in words:
    dic1[word] = len(word)

print(dic1)

# Write a program that takes a string from the user and prints the number of spaces in the string.
str1 = str(input("Please enter a sentence. "))
count1=0
for val in str1:
    if val == " ":
        count1+=1
print(count1)

#Write a program to check whether two lists share no common elements.
list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7, 8,2]
if set(list1).isdisjoint(set(list2)):   # isdisjoint return true in the case of commmon elements otherwise false
    print("no common elements")
else:
    print("contain common elements")