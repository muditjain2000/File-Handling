import numpy as np
A = np.random.randint(2, size=(7))
B = np.random.randint(2, size=(7))
print(A)
print(B)
c = []
for i in range(0, 7):
    if (B[i] != A[i]):
        c.append('True')
    else:
        c.append('False')
print(c)
