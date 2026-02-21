# take a numarical input from the user and make a pyramid
n =5
for val in range(1,n+1):
    for g in range(1, val+1):
        print(g, end='')   # for printing the words in one line

    print()                 # for new line

n = 5

for i in range(1, n+1):
    #print leading spaces
    print(" " * (n - i), end="")  
    #Print ascending numbers
    for j in range(1, i+1):
        print(j, end="")
    #Print descending numbers
    for j in range(i-1, 0, -1):
        print(j, end="")
    # Move to the next line
    print()
k = 10
for q in range(1, k+1):
    print(" "*(k-q), end="")
    for a in range(1,q+1):
        print(a, end='')
    for b in range(q-1,0,-1):
        print(b, end='')
    print()


