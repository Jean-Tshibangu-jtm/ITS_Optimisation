
# Optimizing Autonomous Vehicle Mobility for Flexible and Adaptive Public Transport

## Context

The rise of **autonomous vehicles** and **vehicular networks (VANETs)** is deeply transforming urban mobility. With increasing traffic and the need for smoother transportation, **Intelligent Transportation Systems (ITS)** aim to enhance safety, reliability, and adaptability of mobility.

This research focuses on optimizing **V2I (Vehicle-to-Infrastructure)** communication to improve **Quality of Service (QoS)** for **flexible and adaptive public transport** systems incorporating autonomous vehicles.

## ❗ Problem Statement

Current VANET architectures are rigid and poorly suited to dynamic urban environments. It becomes necessary to:

- **Predict network demand** between vehicles and infrastructure.
- **Dynamically allocate resources** based on that demand.
- Integrate **AI predictive models** to guide this allocation.
- Couple traffic simulation (mobility) and network simulation.

## Testbed Environment

- **Simulators**:
  - `SUMO`: urban mobility simulation.
  - `OMNET++` with `VEINS`: network simulation.
- **Simulated scenarios**: V2I communication in a dense urban setting with dynamic traffic management.
- **Communication technology**: IEEE 802.11p (DSRC).

## Dataset Used

- **Source**: V2I communication traces using IEEE 802.11p.
- **Volume**: 43,631 observations.
- **Content**: transmission power, speed, position, packet delivery rate (PDR), etc.

## Technologies & Tools

- **Simulators**: OMNET++, SUMO, VEINS.
- **Languages**: Python, XML.
- **Frameworks**: TensorFlow, Keras, Jupyter Notebooks.
- **Methods**: Feature engineering, normalization, cross-validation.

## AI & Algorithms Used

Two main approaches:

### 1. Multiple Regression
- Goal: predict the required transmission power.
- Metrics: MAE, RMSE, AIC.

### 2. Deep Learning
- **Artificial Neural Networks (ANN)** to model complex relationships.
- Model accuracy: **98%** (explained variance score).
- 8-fold cross-validation.

## 📈 Results

- The **deep learning** model significantly outperforms multiple regression.
- Strong ability to **accurately predict optimal transmission power** for better QoS.
- Recommendations for **dynamic allocation of V2I network resources**.

## Contributions

- Proposed an **AI-based predictive model** for V2I communication.
- Innovative coupling of **mobility and network simulators**.
- Evaluation through probabilistic connectivity metrics.


## 🔭 Future Work

- Integration of advanced models: **CNNs, LSTM,autoencoders**.
- Development of a real-time embedded system in vehicles.
- Extension to other communication types: V2V, V2P, V2N.

