import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
flattened = a.flatten()
print("Original Array:\\n", a)
print("Flattened Array:", flattened)
