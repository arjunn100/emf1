import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit layout
st.title("Magnetic Field Visualization using Biot-Savart Law")

# User inputs for current
I = st.number_input("Enter the current value (Amps):", value=1.0, step=0.1)

# Define grid
X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

# Constants
mu0 = 4 * np.pi * 1e-7  # Permeability of free space

# Compute the distance from the wire
R = np.sqrt(X**2 + Y**2)
R[R == 0] = 1e-12  # Avoid division by zero by setting a small non-zero value

# Compute magnetic field components based on Biot-Savart Law for an infinite straight wire
Bx = -mu0 * I * Y / (2 * np.pi * R**2)
By = mu0 * I * X / (2 * np.pi * R**2)

# Plot magnetic field using quiver plot (arrow plot)
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Bx, By, color='b')
plt.title(f"Magnetic Field due to Infinite Current Filament (I={I} A)")
plt.xlabel("X-axis (m)")
plt.ylabel("Y-axis (m)")
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Display the plot in Streamlit
st.pyplot(plt)
