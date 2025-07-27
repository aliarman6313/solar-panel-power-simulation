# ☀️ Simple Solar Panel Power Simulation

This project simulates the power output of a basic solar panel system over the course of a day. It models the effects of solar irradiance and temperature on the panel's efficiency.

---

## ⚙️ Features

- Simulates solar irradiance from 6:00 AM to 6:00 PM
- Models temperature-dependent efficiency loss
- Calculates power output based on irradiance and temperature
- Generates plots of:
  - Solar power output (kW)
  - Irradiance (W/m²)
  - Temperature (°C)

---

## 🧠 Physics Background

The power output is given by:

\[
P = A \cdot G \cdot \eta(T)
\]

Where:
- \(A\) = panel area
- \(G\) = solar irradiance
- \(\eta(T) = \eta_{\text{ref}} \cdot (1 - \beta (T - T_{\text{ref}}))\)

---

## 📦 Installation

Install dependencies:

`bash
pip install -r requirements.txt
