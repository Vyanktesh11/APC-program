import numpy as np
marks = np.array([75, 82, 65, 90, 88, 72, 95, 60, 84, 79, 91, 68, 86, 77, 93, 70, 81, 89, 74, 96])
average = np.mean(marks)
print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])
