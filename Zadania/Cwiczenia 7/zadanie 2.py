import numpy as np
a=np.matrix('1 5 8; 3 6 7;6 7 3 ')
b=np.matrix('3 5 6 2; 5 9 2 7; 9 3 5 1; 9 5 3 1')
print(np.amin(b,axis=0))
print(np.amin(b,axis=1))
print(np.amin(a,axis=0))
print(np.amin(a,axis=1))