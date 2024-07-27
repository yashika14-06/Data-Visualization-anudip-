try:
    file = open("yashika.txt",'r')
except FileNotFoundError as e:
    print("file not found")
    print(e)