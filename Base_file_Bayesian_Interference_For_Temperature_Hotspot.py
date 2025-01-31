import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Simulated temperature readings (sensor data)
np.random.seed(42)
n_sensors = 100
background_temp = np.random.normal(25, 2, n_sensors)  # Normal region (mean=25°C, std=2)
hotspot_temp = np.random.normal(40, 3, 5)  # Hotspot region (mean=40°C, std=3)
temperatures = np.concatenate([background_temp, hotspot_temp])

# Define prior (assume hotspots are rare)
prior_mean = 30  # Prior belief of average temperature
prior_std = 5    # Uncertainty in prior
prior = norm(prior_mean, prior_std)

# Likelihood function (assumes Gaussian noise)
likelihood_std = 2  # Measurement noise

# Compute Posterior using Bayes' Rule
posterior_means = []
posterior_stds = []

for temp in temperatures:
    likelihood = norm(temp, likelihood_std)
    posterior_mean = (prior_mean / prior_std**2 + temp / likelihood_std**2) / (1 / prior_std**2 + 1 / likelihood_std**2)
    posterior_std = np.sqrt(1 / (1 / prior_std**2 + 1 / likelihood_std**2))
    posterior_means.append(posterior_mean)
    posterior_stds.append(posterior_std)

# Convert to numpy arrays
posterior_means = np.array(posterior_means)
posterior_stds = np.array(posterior_stds)

# Identify hotspots (posterior mean above threshold)
threshold = 35
hotspots = posterior_means > threshold

# Plot results
plt.figure(figsize=(10, 5))
sns.kdeplot(temperatures, label="Observed Temperatures", fill=True, color="blue", alpha=0.3)
sns.kdeplot(posterior_means, label="Posterior Estimates", fill=True, color="red", alpha=0.3)
plt.axvline(threshold, color="black", linestyle="--", label="Hotspot Threshold")
plt.xlabel("Temperature (°C)")
plt.ylabel("Density")
plt.legend()
plt.title("Bayesian Inference for Temperature Hotspot Detection")
plt.show()

# Print detected hotspots
print(f"Detected {hotspots.sum()} hotspots out of {n_sensors} sensors.")
