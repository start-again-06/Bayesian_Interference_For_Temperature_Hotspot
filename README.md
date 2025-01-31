🔥 Temperature Hotspot Detection & Tracking

📌 Overview

This repository contains implementations of Bayesian Inference, Gaussian Processes, Kalman Filters, and Particle Filters for detecting and tracking temperature hotspots over time and space. The techniques are applied to simulated sensor data. 📊

🚀 Features

Bayesian Inference: Probabilistic hotspot detection using prior and likelihood models. 🎯

Gaussian Processes: 2D spatial temperature estimation with smooth interpolation. 🌎

Kalman Filters: Time-series tracking of hotspots with noise reduction. 📈

Particle Filters: Probabilistic evolution of hotspots over time. 🔄

Visualization: Interactive plots and heatmaps for better insight. 🎨

🔧 Installation

📦 Dependencies

Ensure you have the following Python libraries installed:

[pip install numpy matplotlib seaborn scipy scikit-learn pykalman](url)

🏗️ How It Works

1️⃣ Bayesian Inference for Hotspot Detection

Assumes hotspots are rare (prior belief 🎯).

Uses sensor readings to update posterior probabilities.

Identifies hotspots where posterior mean > threshold.

2️⃣ Gaussian Process Regression (GPR)

Models temperature field using Radial Basis Function (RBF) kernel.

Predicts temperature across a 2D spatial grid.

Detects hotspots where predicted mean > 35°C 🔥.

3️⃣ Kalman Filter for Time-Series Hotspot Tracking

Processes sensor temperature readings over time ⏳.

Estimates true temperature by filtering noisy observations.

Tracks hotspot activation over time steps.

4️⃣ Particle Filter for Probabilistic Hotspot Evolution

Uses Monte Carlo-based simulation for hotspot tracking 🎲.

Predicts future temperature states based on process and measurement noise.

Resamples particles based on likelihood updates.

📊 Results & Visualization

Each method generates visualizations such as:

Density plots: Show probability distributions of temperature readings.

Heatmaps: Highlight hotspot locations and intensities.

Time-series graphs: Compare raw vs. filtered temperature data.

📢 Contribution

Feel free to fork and contribute to improve the models or visualizations! 🛠️


