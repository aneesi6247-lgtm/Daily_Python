# write a whole sentence and count the frequency of each word and and full dictionry with all the words

sent = "Python is great and python is powerful and Python is easy"

sent=sent.lower()
abc = sent.split()
dic = {}
for val in abc:
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1
print(dic)

count =0
frq = None
for key,val in dic.items():
    if val > count:
        count = val
        frq = key
print (" the maximum value is:", frq)
print ("The frequency of this is:", count)
