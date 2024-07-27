a=int(input("enter the dividend : "))
b=int(input("Enter the divisior : "))

try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("ZeroDivisionError")
    print("enter the valid inputs")
