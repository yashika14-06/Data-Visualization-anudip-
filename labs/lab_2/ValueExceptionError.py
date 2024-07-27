
try:
    a = int(input("Enter an integer value : "))
    print(a)
except ValueError as e:
    print("Value Error")
    print(e)