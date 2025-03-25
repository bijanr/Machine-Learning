import numpy as np

# ar1 = np.arange(10, 22)
# print(ar1.reshape(4,3))

# split
# ar2 = np.array([[10, -7, 0, 20], [5, 1, 200, 40], [6, 9, 39, 1], [67, 25, 36, 93], [2, 3, -7, 0]])
# print(ar2)
# first, second, third = np.split(ar2, [2, 3])
# print('first' , first)
# print('second', second)
# print('third',third)


# A = np.array([1, 2, 3, 4, 5, 6])
# B = np.array([[1, 2, 3], [4, 5, 6]])
# print(A.max(axis=0))

fileLoad = np.loadtxt("nigga.txt", dtype=int, delimiter=',')
print(fileLoad)
