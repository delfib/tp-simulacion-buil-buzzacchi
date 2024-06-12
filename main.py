
from integration_methods.euler import EulerMethod
from integration_methods.trapezoidal import TrapezoidalMethod
from plotter import plot_results
from simulation import Simulation
from configparser import ConfigParser

def main():

    config = ConfigParser()
    config.read('config.ini')

    initial_height = config.getfloat('simulation', 'initial_height')
    initial_velocity = config.getfloat('simulation', 'initial_velocity')
    h = config.getfloat('simulation', 'h')
    ba = config.getfloat('params', 'ba')
    m = config.getfloat('params', 'm')
    b = config.getfloat('params', 'b')
    g = config.getfloat('params', 'g')
    k = config.getfloat('params', 'k')

    euler_simulation = Simulation(EulerMethod, initial_height, initial_velocity, h, ba, m , b, g, k)
    trapezoidal_simulation = Simulation(TrapezoidalMethod, initial_height, initial_velocity, h, ba, m , b, g, k)

    euler_height_values, euler_velocity_values = euler_simulation.run()
    trapezoidal_height_values, trapezoidal_velocity_values = trapezoidal_simulation.run()

    # Extract data for plotting

    times_euler = list(euler_height_values.keys())
    heights_euler = list(euler_height_values.values())
    velocities_euler = list(euler_velocity_values.values())

    times_trapezoidal = list(trapezoidal_height_values.keys())
    heights_trapezoidal = list(trapezoidal_height_values.values())
    velocities_trapezoidal = list(trapezoidal_velocity_values.values())

    # Plot the results
    plot_results(times_euler, heights_euler, velocities_euler, times_trapezoidal, heights_trapezoidal, velocities_trapezoidal)  


if __name__ == "__main__":
    main()

