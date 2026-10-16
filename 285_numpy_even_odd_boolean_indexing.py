import numpy as np
a = np.arange(1, 21)
print("Array:", a)
print("Even Numbers:", a[a % 2 == 0])
print("Odd Numbers:", a[a % 2 != 0])
