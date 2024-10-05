import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Magnetic Field Calculation using Biot-Savart Law")

# Step 1: User Input
st.header("Step 1: Enter the current value (in Amps)")

# Input for current value (I)
I = st.number_input("Enter the current value (in Amps):", value=1.0, step=0.1)

# Button to trigger the calculation
if st.button("Calculate Magnetic Field"):

    # Step 2: Magnetic Field Calculation and Visualization
    st.header("Step 2: Magnetic Field Calculation and Output")

    # Define the grid for the field (x, y coordinates)
    X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

    # Constants
    mu0 = 4 * np.pi * 1e-7  # Permeability of free space

    # Compute the distance from the wire
    R = np.sqrt(X**2 + Y**2)
    R[R == 0] = 1e-12  # Avoid division by zero by setting a small non-zero value

    # Compute magnetic field components based on Biot-Savart Law
    Bx = -mu0 * I * Y / (2 * np.pi * R**2)
    By = mu0 * I * X / (2 * np.pi * R**2)

    # Plot the magnetic field using quiver (arrow plot)
    plt.figure(figsize=(6, 6))
    plt.quiver(X, Y, Bx, By, color='blue')
    plt.title(f"Magnetic Field due to Infinite Current Filament (I={I} A)")
    plt.xlabel("X-axis (m)")
    plt.ylabel("Y-axis (m)")
    plt.grid(True)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    # Display the plot in Streamlit
    st.pyplot(plt)
