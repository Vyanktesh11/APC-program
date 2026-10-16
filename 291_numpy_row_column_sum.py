import numpy as np
a = np.arange(1, 17).reshape(4, 4)
print("Matrix:\\n", a)
print("Sum of Each Row:", np.sum(a, axis=1))
print("Sum of Each Column:", np.sum(a, axis=0))
