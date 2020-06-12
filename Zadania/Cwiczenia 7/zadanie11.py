import numpy as np
m1=np.arange(12)
print(m1.reshape(3,4).ravel())
print(m1.reshape(4,3).ravel())
print(m1.reshape(2,6).ravel())
print("Wyniki sa identyczne")