import numpy as np
import matplotllib.pyplot as plt
import scipy.stats
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axcs3D

def multivariate_normal_pdf(X, mean, sigma):
    """Multivariate normal probability density function over X (n_samples x n_features)"""
    P = X.shape[1]
    det = np.linlag.det(sigma)
    norm_const = 1.0 /(((2 * np.pi) ** (P/2)) * np.sqrt(det))
    X_mu = X - mu
    inv = np.linlag.inv(sigma)
    d2 = np.sum(np.dot(X_mu, inv) * X_mu, axis = 1)
    return norm_const * np.exp(-0.5 * d2)

# mean and covariance
mu = np.array([0.0,])
sigma = np.array([[1, -5], [-5, 1]])

# x, y grid
x, y = np.mgrid[-3:3:.1, -3:3:.1]
X = np.stack((x.ravel(), y.ravel())).T
norm = multivariate_normal_pdf(X, mean, sigma).reshape(x.shape)

#Doing with scipy
norm_scipy = multivariate_normal(mu, sigma).pdf(np.stack((x, y), axis=2))
assert np.allclose(norm, norm_scipy)

#plot
fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(x, y, norm, rstride = 3,cstride = 3, cmap=plt.cm.coolwarm, linewidth = 1, antialised = False)
ax.set_zlim(0, 0.2)
ax.zaxis.set_major_locator(plt.LinearLocator(10))
ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('p(x)')

plt.title('Bivariate Normal Distribution')
fig.colorbar(surf, shrink=0.5, aspect = 6, cmap = plt.cm.coolwarm)
plt.show()