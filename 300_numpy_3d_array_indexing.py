import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("First Element:", a[0, 0, 0])
print("Last Element:", a[-1, -1, -1])
print("Element at [0,1,2]:", a[0, 1, 2])
print("Element at [1,2,3]:", a[1, 2, 3])
