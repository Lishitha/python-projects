"""num = int(input("enter a number"))

if num < 0:
    print("nmbr is negtv")
elif num == 0:
    print("nmbr is zero")
else:
    print("nmber id postv")"""

menu = ["meals","biriyani","ghee rice"]
print(menu)
order =int(input("menu number : "))
if order == 1:
    print("meals")
elif order == 2:
    print("biriyani")
elif order == 3:
    print("ghee rice")
else:
    print("not available")