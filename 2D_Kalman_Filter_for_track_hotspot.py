import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pykalman import KalmanFilter


np.random.seed(42)
timesteps = 50
n_sensors = 20
grid_size = 50  


sensor_x = np.random.uniform(0, grid_size, n_sensors)
sensor_y = np.random.uniform(0, grid_size, n_sensors)

background_temp = np.random.normal(25, 2, (timesteps, n_sensors))  # Normal temp fluctuations
hotspot_indices = np.random.choice(n_sensors, size=3, replace=False)  # 3 sensors as hotspots
hotspot_temp = np.random.normal(40, 3, (timesteps, len(hotspot_indices)))  # Hotspots fluctuate

for i, idx in enumerate(hotspot_indices):
    background_temp[:, idx] = hotspot_temp[:, i]


kf = KalmanFilter(
    transition_matrices=np.array([[1]]), 
    observation_matrices=np.array([[1]]),  
    transition_covariance=np.array([[0.5]]),  
    observation_covariance=np.array([[2]]),
    initial_state_mean=np.mean(background_temp[0]),  
    initial_state_covariance=np.array([[1]]) 
)


filtered_temps = []
for i in range(n_sensors):
    measurements = background_temp[:, i].reshape(-1, 1)
    state_means, _ = kf.filter(measurements) 
    filtered_temps.append(state_means.flatten())

filtered_temps = np.array(filtered_temps).T  


threshold = 35
hotspots_over_time = filtered_temps > threshold


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
sensor_idx = hotspot_indices[0] 
plt.plot(range(timesteps), background_temp[:, sensor_idx], label="Raw Sensor Data", alpha=0.5)
plt.plot(range(timesteps), filtered_temps[:, sensor_idx], label="Kalman Filtered Estimate", linewidth=2)
plt.axhline(threshold, color="r", linestyle="--", label="Hotspot Threshold")
plt.xlabel("Time Steps")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title(f"Kalman Filter for Sensor {sensor_idx}")

plt.subplot(1, 2, 2)
sns.heatmap(hotspots_over_time.T, cmap="Reds", cbar=False, xticklabels=5, yticklabels=False)
plt.xlabel("Time Steps")
plt.ylabel("Sensor Index")
plt.title("Hotspot Activation Over Time")

plt.tight_layout()
plt.show()

print(f"Hotspots detected in {hotspots_over_time.sum()} instances over {timesteps} time steps.")
