import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit layout
st.title("Magnetic Field Visualization using Biot-Savart Law")

# User inputs for current
I = st.number_input("Enter the current value (Amps):", value=1.0)

# Define grid
X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

# Constants
mu0 = 4 * np.pi * 1e-7  # Permeability of free space

# Distance from the wire
R = np.sqrt(X**2 + Y**2)
R[R == 0] = 1e-12  # Avoid division by zero

# Magnetic field based on Biot-Savart Law
Bx = -mu0 * I * Y / (2 * np.pi * R**2)
By = mu0 * I * X / (2 * np.pi * R**2)

# Plot magnetic field
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Bx, By)
plt.title(f"Magnetic Field due to Infinite Current Filament (I={I} A)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
st.pyplot(plt)
