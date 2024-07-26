import numpy as np

#find the total revenue
lis_1 = [500,600,700,550]
lis_2 = [450 , 700 , 800 , 600]
category_product_1 = np.array(lis_1)
category_product_2 = np.array(lis_2)
print(category_product_1+category_product_2)

#find the profit
revenue = np.array([10000,12000,11000,10500])
expenses = np.array([4000,5000,4500,4800])
print(revenue - expenses)

#determine which products in a store are out of stock
inventory = np.array([10,0,5,0,20,0])
for i in range(len(inventory)):
    if i == 0:
        print(np.where(inventory == i))
print(inventory[inventory == 0])
#total cost of the shopping cart
quantity = np.array([2,3,4,1])
price_per_item = np.array([10.0 , 5.0 , 8.0 , 12.0],dtype='int')
price = quantity*price_per_item
print(price)

