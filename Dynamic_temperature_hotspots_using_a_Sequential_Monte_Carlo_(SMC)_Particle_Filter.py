import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(42)
timesteps = 50
n_sensors = 20
grid_size = 50 
n_particles = 500 


sensor_x = np.random.uniform(0, grid_size, n_sensors)
sensor_y = np.random.uniform(0, grid_size, n_sensors)


background_temp = np.random.normal(25, 2, (timesteps, n_sensors))  # Normal temperature
hotspot_indices = np.random.choice(n_sensors, size=3, replace=False)  # 3 Hotspot sensors
hotspot_temp = np.random.normal(40, 3, (timesteps, len(hotspot_indices)))

for i, idx in enumerate(hotspot_indices):
    background_temp[:, idx] = hotspot_temp[:, i]

particles = np.random.uniform(20, 50, (n_particles, n_sensors))
weights = np.ones(n_particles) / n_particles


process_noise = 1.0 
measurement_noise = 2.0


filtered_estimates = np.zeros((timesteps, n_sensors))


for t in range(timesteps):
  
    particles += np.random.normal(0, process_noise, particles.shape)  
    
 
    sensor_readings = background_temp[t, :]  
    likelihood = np.exp(-0.5 * ((particles - sensor_readings) ** 2) / measurement_noise**2)
    weights *= likelihood.prod(axis=1)  
    weights += 1e-6 
    weights /= weights.sum() 

  
    indices = np.random.choice(np.arange(n_particles), size=n_particles, p=weights)
    particles = particles[indices]
    weights.fill(1.0 / n_particles)

 
    filtered_estimates[t, :] = np.mean(particles, axis=0)

threshold = 35
hotspot_mask = filtered_estimates > threshold


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
sensor_idx = hotspot_indices[0] 
plt.plot(range(timesteps), background_temp[:, sensor_idx], label="Raw Sensor Data", alpha=0.5)
plt.plot(range(timesteps), filtered_estimates[:, sensor_idx], label="Particle Filter Estimate", linewidth=2)
plt.axhline(threshold, color="r", linestyle="--", label="Hotspot Threshold")
plt.xlabel("Time Steps")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title(f"Particle Filter Tracking for Sensor {sensor_idx}")

plt.subplot(1, 2, 2)
sns.heatmap(hotspot_mask.T, cmap="Reds", cbar=False, xticklabels=5, yticklabels=False)
plt.xlabel("Time Steps")
plt.ylabel("Sensor Index")
plt.title("Hotspot Activation Over Time")

plt.tight_layout()
plt.show()

print(f"Hotspots detected in {hotspot_mask.sum()} instances over {timesteps} time steps.")
