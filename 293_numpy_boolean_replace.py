import numpy as np
a = np.array([12, 65, 34, 78, 50, 91, 23, 56, 44, 82])
a[a > 50] = 0
print("Updated Array:", a)
