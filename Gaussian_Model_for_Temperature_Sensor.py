import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import cdist
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel


np.random.seed(42)
n_sensors = 50
grid_size = 50  

sensor_x = np.random.uniform(0, grid_size, n_sensors)
sensor_y = np.random.uniform(0, grid_size, n_sensors)


background_temp = np.random.normal(25, 2, n_sensors)  
hotspot_indices = np.random.choice(n_sensors, size=5, replace=False) 
hotspot_temp = np.random.normal(40, 3, len(hotspot_indices))
temperatures = background_temp
temperatures[hotspot_indices] = hotspot_temp  


kernel = 1.0 * RBF(length_scale=10) + WhiteKernel(noise_level=2)
gp = GaussianProcessRegressor(kernel=kernel)


sensor_positions = np.vstack((sensor_x, sensor_y)).T
gp.fit(sensor_positions, temperatures)


x_grid = np.linspace(0, grid_size, grid_size)
y_grid = np.linspace(0, grid_size, grid_size)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
grid_points = np.vstack((X_grid.ravel(), Y_grid.ravel())).T


pred_mean, pred_std = gp.predict(grid_points, return_std=True)
pred_mean = pred_mean.reshape(grid_size, grid_size)
pred_std = pred_std.reshape(grid_size, grid_size)

# Identify hotspots (posterior mean > 35°C)
hotspot_mask = pred_mean > 35


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.contourf(X_grid, Y_grid, pred_mean, cmap="hot", levels=50)
plt.colorbar(label="Predicted Temperature (°C)")
plt.scatter(sensor_x, sensor_y, c=temperatures, cmap="coolwarm", edgecolors="k", label="Sensors")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Predicted Temperature Field")
plt.legend()


plt.subplot(1, 2, 2)
plt.contourf(X_grid, Y_grid, hotspot_mask, cmap="Reds", alpha=0.6)
plt.colorbar(label="Hotspot Probability")
plt.scatter(sensor_x, sensor_y, c=temperatures, cmap="coolwarm", edgecolors="k", label="Sensors")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Hotspot Detection Map")
plt.legend()

plt.tight_layout()
plt.show()
