import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of All Elements:", np.sum(a))
print("Sum of Each Layer:\\n", np.sum(a, axis=(1, 2)))
print("Sum Along Rows:\\n", np.sum(a, axis=2))
print("Sum Along Columns:\\n", np.sum(a, axis=1))
