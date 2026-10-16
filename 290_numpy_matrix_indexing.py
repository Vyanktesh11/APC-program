import numpy as np
a = np.arange(1, 17).reshape(4, 4)
print("Matrix:\\n", a)
print("First Row:", a[0])
print("Last Column:", a[:, -1])
print("Diagonal Elements:", np.diag(a))
print("Second and Third Rows:\\n", a[1:3])
