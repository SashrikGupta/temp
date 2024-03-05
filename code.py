import matplotlib.pyplot as plt
import numpy as np

# Function to generate and save the sine wave plot

a = 5 

def generate_sine_plot():

    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)

    plt.plot(x, y, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Sine Function Plot')
    plt.legend()

    plt.subplots()


