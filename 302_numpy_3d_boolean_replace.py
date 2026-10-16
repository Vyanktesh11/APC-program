import numpy as np
a = np.random.randint(1, 101, size=(2, 3, 4))
print("Original Array:\\n", a)
a[a > 50] = 0
print("Updated Array:\\n", a)
