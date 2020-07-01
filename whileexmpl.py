"""i = 11
while i <= 5:
    print(i)
    i+=1
else :
    print("finished")"""

i=1
n =int(input("enter the number of rows"))

while i <= n:
    sp = n - i
    while sp>0:
        print(end=" ")
        sp = sp-1
    star = i
    while star > 0:
        print("*")
        #print(" ")
        star = star-1
    i = i+1

