import numpy as np


a = np.array(list(map(float, input().split())))
b = np.array(list(map(float, input().split())))
c = np.array(list(map(float, input().split())))
d = np.array(list(map(float, input().split())))
ac = c - a
bd = d - b
n1 = np.linalg.norm(np.cross((b - a), bd)) / np.linalg.norm(np.cross(ac, bd))
e = a + ac * n1
ae = e - a
f = c - ae
m1 = (b + d) * 0.5
fm1 = m1 - f
m = f + fm1 * (2 / 3)
print(m)
