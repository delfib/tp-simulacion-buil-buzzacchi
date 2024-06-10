import matplotlib.pyplot as plt

MIN_HEIGHT = 0.00001

def plot_results(times_euler, heights_euler, velocities_euler, times_trapezoidal, heights_trapezoidal, velocities_trapezoidal):
    """Plot height and velocity over time using both Euler and Trapezoidal methods."""
    plt.figure(figsize=(12, 6))

    # Plot Height
    plt.subplot(2, 1, 1)
    plt.plot(times_euler, heights_euler, label='Euler Method', color='b')
    plt.plot(times_trapezoidal, heights_trapezoidal, label='Trapezoidal Method', color='r')
    plt.axhline(MIN_HEIGHT, color='g', linestyle='--', label='Min Height')
    plt.xlabel('Time')
    plt.ylabel('Height (m)')
    plt.title('Height')
    plt.legend()
    plt.grid(True)

    # Plot Velocity
    plt.subplot(2, 1, 2)
    plt.plot(times_euler, velocities_euler, label='Euler Method', color='b')
    plt.plot(times_trapezoidal, velocities_trapezoidal, label='Trapezoidal Method', color='r')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('simulation_plot.png')
