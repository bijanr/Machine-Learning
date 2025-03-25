import numpy as np

a1 = np.array([[10, 20], [-30, 40]])
a2 = np.zeros([2, 3])

print(np.concatenate((a1, a2), axis=1))