#Remove the duplicate without using set
#count how many time each number appears
#Print the numbers that appears the most
numbers = [4, 7, 2, 9, 7, 2, 1, 9, 9, 3]
arry = []
for val in numbers:
    if val not in arry:
        arry.append(val)
print(arry)

dic={}
for val in numbers:
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1
print(dic)

max_count= 0
max_Freq= None
for key, val in dic.items():
    if val>max_count:
        max_count = val
        max_Freq = key
print("the maximum value is:", max_Freq)
print("the Frequency is: ", max_count)
