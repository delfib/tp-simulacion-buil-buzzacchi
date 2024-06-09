
from integration_methods.euler import EulerMethod
from integration_methods.heun import HeunMethod
# from integration_methods.trapezoidal import TrapezoidalMethod
from plotter import plot_results
from simulation import Simulation

def main():
    initial_height = 10
    initial_velocity = 0
    h = 0.0001

    euler_simulation = Simulation(EulerMethod, initial_height, initial_velocity, h)
    heun_simulation = Simulation(HeunMethod, initial_height, initial_velocity, h)
    # trapezoidal_simulation = Simulation(TrapezoidalMethod, initial_height, initial_velocity, h)

    euler_height_values, euler_velocity_values = euler_simulation.run()
    # heun_height_values, heun_velocity_values = heun_simulation.run()
    # trapezoidal_height_values, trapezoidal_velocity_values = trapezoidal_simulation.run()

    # Extract data for plotting

    times_euler = list(euler_height_values.keys())
    heights_euler = list(euler_height_values.values())
    velocities_euler = list(euler_velocity_values.values())

    # times_heun = list(heun_height_values.keys())
    # heights_heun = list(heun_height_values.values())
    # velocities_heun = list(heun_velocity_values.values())

    # times_trapezoidal = list(trapezoidal_height_values.keys())
    # heights_trapezoidal = list(trapezoidal_height_values.values())
    # velocities_trapezoidal = list(trapezoidal_velocity_values.values())

    # Plot the results
    plot_results(times_euler, heights_euler, velocities_euler)


if __name__ == "__main__":
    main()

