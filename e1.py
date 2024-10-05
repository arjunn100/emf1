import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit layout
st.title("Magnetic Field Calculation using Biot-Savart Law")

# Step 1: Enter the value
st.header("Step 1: Enter the current value")

# User input for current in Amps
I = st.number_input("Enter the current value (Amps):", value=1.0, step=0.1)

# Button to proceed to calculation
if st.button("Calculate Magnetic Field"):
    # Step 2: Calculation and Output
    st.header("Step 2: Magnetic Field Calculation")
    
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
    plt.title(f"Magnetic Field due

