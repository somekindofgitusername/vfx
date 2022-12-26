import math
import matplotlib.pyplot as plt

# Define the function
def emissivity(λ, T):
    # Calculate the emissivity of the material using the Planck equation
    return (2.0 * 6.62607015e-34 * math.pow(299792458.0, 2.0) / math.pow(λ, 5.0)) * 1.0 / (math.exp(6.62607015e-34 * 299792458.0 / (λ * 1.380649e-23 * T)) - 1.0)

# Define the input variables
λ = 550.0e-9 # Wavelength of the electromagnetic radiation in meters (m) (assumed value)

# Define the range of temperatures to plot
temperatures = range(273, 323)

# Calculate the emissivity of water at each temperature
emissivities = [emissivity(λ, T) for T in temperatures]

# Plot the emissivity of water over the range of temperatures
plt.plot(temperatures, emissivities)

# Add axis labels and a title to the plot
plt.xlabel("Temperature (K)")
plt.ylabel("Emissivity")
plt.title("Emissivity of Water over a Range of Temperatures")

# Show the plot
plt.show()
