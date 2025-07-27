import numpy as np
import matplotlib.pyplot as plt

# ---------- 1. مشخصات پنل ----------
panel_area = 1.6  # m²
eta_ref = 0.18    # راندمان مرجع (18%)
beta = 0.004      # ضریب کاهش راندمان (درجه C⁻¹)
T_ref = 25        # دمای مرجع (درجه سلسیوس)

# ---------- 2. شرایط محیطی ----------
# زمان از 6 صبح تا 6 عصر (هر 10 دقیقه)
time = np.linspace(6, 18, 72)
solar_irradiance = np.maximum(0, 1000 * np.sin(np.pi * (time - 6) / 12))  # W/m²
temperature = 25 + 10 * np.sin(np.pi * (time - 6) / 12)  # دما (از 25 تا 35 درجه در ظهر)

# ---------- 3. محاسبه بازده واقعی ----------
eta_actual = eta_ref * (1 - beta * (temperature - T_ref))

# ---------- 4. محاسبه توان خروجی ----------
power_output = panel_area * solar_irradiance * eta_actual  # W

# ---------- 5. نمودار ----------
plt.figure(figsize=(10, 6))
plt.plot(time, power_output / 1000, label="Power Output [kW]", color='orange')
plt.plot(time, solar_irradiance, '--', label="Irradiance [W/m²]", color='blue')
plt.plot(time, temperature, ':', label="Temperature [°C]", color='red')

plt.title("Simulated Solar Panel Output")
plt.xlabel("Time of Day [hr]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("solar_output.png")
plt.show()