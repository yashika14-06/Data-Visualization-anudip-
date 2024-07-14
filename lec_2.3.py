sp = float(input("enter the selling price"))
cp = float(input("enter the cost price"))
if(sp < 0):
    print("invalid")
elif(cp < 0):
    print("invalid")
if(sp > cp):
    print("profit of : ",sp-cp)
else:
    print("loss of :" , cp-sp)