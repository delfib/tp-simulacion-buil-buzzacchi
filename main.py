
from integration_methods.euler import EulerMethod
from integration_methods.heun import HeunMethod
from integration_methods.trapezoidal import TrapezoidalMethod
from plotter import plot_results
from simulation import Simulation

def main():
    initial_height = 10
    initial_velocity = 0
    h = 0.0001

    euler_simulation = Simulation(EulerMethod, initial_height, initial_velocity, h)
    trapezoidal_simulation = Simulation(TrapezoidalMethod, initial_height, initial_velocity, h)

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
    #plot_results(times_trapezoidal, heights_trapezoidal, velocities_trapezoidal)

    # Calculate differents values
    """ time_points = sorted(list(set(euler_height_values.keys()) & set(trapezoidal_height_values.keys())))
    
    height_differences = []
    velocity_differences = []
    
    for t in time_points:
        height_difference = abs(euler_height_values[t] - trapezoidal_height_values[t])
        velocity_difference = abs(euler_velocity_values[t] - trapezoidal_velocity_values[t])
        
        height_differences.append(height_difference)
        velocity_differences.append(velocity_difference)
        
    max_height_difference = max(height_differences)
    max_velocity_difference = max(velocity_differences)
    
    avg_height_difference = sum(height_differences) / len(height_differences)
    avg_velocity_difference = sum(velocity_differences) / len(velocity_differences)
    
    print("Comparación de resultados entre Euler y Trapezoidal:")
    print("----------------------------------------------------")
    print("Diferencia máxima de altura:", max_height_difference)
    print("Diferencia máxima de velocidad:", max_velocity_difference)
    print("Diferencia promedio de altura:", avg_height_difference)
    print("Diferencia promedio de velocidad:", avg_velocity_difference) """
    
    


if __name__ == "__main__":
    main()

