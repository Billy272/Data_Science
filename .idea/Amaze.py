from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

plt.style.use('_mpl-gallery')

n_radii=8
n_angles=36

radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=True)

x=np.append(0, (radii*np.cos(angles)).flatten())
y=np.append(0, (radii*np.sin(angles)).flatten())
z=np.sin(-x*y)

fig, ax = plt.subplots(subplot_kw={'axes':ax})
ax.plot(x, y, z, vmin=z.min()*2, cmap='gray')

ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()