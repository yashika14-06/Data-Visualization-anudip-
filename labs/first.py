import numpy as np
lis = [1,2,3,4,5,6]
ar = np.array(lis)
print(ar[0])
print(ar[-1])
print(ar*2)
arr = np.zeros(10,dtype='int')
print(arr)
arr_1 = np.ones(10,dtype='int')
print(arr_1)
arr_2 = np.ones(10,dtype='int')*5
print(arr_2)
arr_3 = np.arange(2,11).reshape(3,3)
print(arr_3)
