import numpy as np
a = np.random.randint(1, 101, size=(3, 4, 5))
flattened = a.flatten()
average = np.mean(flattened)
print("Original 3D Array:\\n", a)
print("Values Greater Than 50:", flattened[flattened > 50])
print("Even Numbers:", flattened[flattened % 2 == 0])
print("Values Less Than Average:", flattened[flattened < average])
