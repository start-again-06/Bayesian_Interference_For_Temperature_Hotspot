# Temperature Hotspot Detection & Tracking

---

## System Overview
This repository implements **Bayesian Inference, Gaussian Processes, Kalman Filters, and Particle Filters** for detecting and tracking temperature hotspots over time and space. The methods are applied to simulated sensor data to identify, estimate, and track hotspot dynamics.

---

## High-Level Architecture

### Detection & Estimation Layer
- **Bayesian Inference:** Probabilistic hotspot detection using prior and likelihood models  
- **Gaussian Processes (GPR):** 2D spatial temperature estimation with smooth interpolation  

### Time-Series Tracking Layer
- **Kalman Filters:** Noise reduction and temporal tracking of hotspots  
- **Particle Filters:** Probabilistic evolution of hotspots over time using Monte Carlo simulations  

### Visualization Layer
- Interactive plots, density plots, heatmaps, and time-series graphs for analysis and monitoring  

---

## Execution Flow

1. **Bayesian Inference**
   - Assumes hotspots are rare (prior belief)  
   - Updates posterior probabilities with sensor readings  
   - Identifies hotspots where posterior mean exceeds a threshold  

2. **Gaussian Process Regression (GPR)**
   - Models temperature field with RBF kernel  
   - Predicts temperature over a 2D grid  
   - Detects hotspots where predicted mean > 35°C  

3. **Kalman Filter**
   - Filters noisy time-series sensor data  
   - Estimates true temperature over time  
   - Tracks activation and evolution of hotspots  

4. **Particle Filter**
   - Simulates hotspot evolution probabilistically  
   - Resamples particles based on measurement likelihood  
   - Predicts future temperature states under uncertainty  

---

## Results & Visualization
- **Density plots:** Show probability distributions of temperature readings  
- **Heatmaps:** Highlight hotspot locations and intensities  
- **Time-series graphs:** Compare raw vs. filtered temperature data  

---

## Scalability & Extensibility
- Can integrate real sensor data for live monitoring  
- Extendable to multi-dimensional sensor networks  
- Supports additional probabilistic or machine learning–based tracking methods  

---

## Applications
- Environmental monitoring and hotspot detection  
- Sensor network data analysis  
- Real-time anomaly detection in temperature fields  
- Educational demonstrations of Bayesian and probabilistic filtering  

---

## Contribution
Feel free to fork and contribute to improve models, visualizations, or performance!   

---

## License
MIT License. Free to use, modify, and distribute for academic and research purposes.
