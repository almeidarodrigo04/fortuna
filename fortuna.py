import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(theta), np.sin(phi))
y = 10 * np.outer(np.sin(theta), np.sin(phi))
z = 10 * np.outer(np.ones(np.size(theta)), np.cos(phi))

# Plot the surface
ax.plot_surface(x, y, z, alpha=0.4)

# Set an equal aspect ratio
ax.set_aspect('equal')

plt.show()