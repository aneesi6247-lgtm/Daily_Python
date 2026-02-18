#Write a program that:
	#1.	Takes a sentence from user
	#2.	Counts how many times each word appears
	#3.	Prints result in dictionary form

snt = str(input("Please Enter the string"))
word = snt.split()                  # it will split the string into the words
print(word)
dic = {}
for val in word:
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1
print(dic)

