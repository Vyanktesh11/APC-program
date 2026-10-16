import numpy as np
a = np.arange(1, 28).reshape(3, 3, 3)
flattened = a.flatten()
print("Flattened Array:", flattened)
print("Sum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))
