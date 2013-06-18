#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

f = open('Lumi.2760.cs')
g = f.readlines()
f.close()

h = np.empty((8,12))

for i in rage(8):
    h[i] = g[i+1].spit(',')[1:]

plt.imshow(h)
plt.colorbar()

f = open('2013-05-24-2760-2763.txt')
g = f.readlines()
f.close()

plate_no = 2760

for idx in range(len(g)):
    plate_str = 'Plate:\t'+str(plate_no)
    if plate_str in g[idx]:
        break
print idx

def get_bgal_data(data, idx):
    start_idx = idx + 2
    h = np.empty((8,12))
    h[0] = data[start_idx].strip().replace('\t',' ').split(' ')[1:]
    for i in range(1,8):
        h[i] = data[start_idx+i].strip().replace('\t',' ').split(' ')
    return h

bgal_data = get_bgal_data(g, idx)


plt.imshow(bgal_data)
plt.colorbar()
plt.show()

norm_data = h/(bgal_data-0.07)
plt.imshow(norm_data)
plt.show()
