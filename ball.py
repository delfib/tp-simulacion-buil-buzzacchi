import matplotlib.pyplot as plt

MAX_TIME = 100
MIN_HEIGHT = 0.00001
MIN_VELOCITY = 0.0001
H = 0.0001

ba = 0.1    
m = 1
b = 30
g = 9.8
k = 100000

# Dictionaries to store height and velocity values
height_values_euler = {}
velocity_values_euler = {}
height_values_trapezoidal = {}
velocity_values_trapezoidal = {}


def run(method):
    if method == 'euler':
        calculate_with_euler()
    elif method == 'trapezoidal':
        calculate_with_trapezoidal()
    else:
        raise ValueError("Unsuported method")


def calculate_with_euler():
    time = 0

    height_values_euler[time] = 10
    velocity_values_euler[time] = 0

    while time <= MAX_TIME:
        next_time = time + H

        height_values_euler[next_time] = get_next_height_euler(time)
        velocity_values_euler[next_time] = get_next_velocity_euler(time)
        
        time = next_time

        if height_values_euler[next_time] < MIN_HEIGHT and abs(velocity_values_euler[next_time]) < MIN_VELOCITY:
            break


def calculate_with_trapezoidal():
    time = 0

    height_values_trapezoidal[time] = 10
    velocity_values_trapezoidal[time] = 0
    height_values_euler[time] = 10
    velocity_values_euler[time] = 0
    
    while time <= MAX_TIME:
        next_time = time + H

        height_values_euler[next_time] = get_next_height_euler(time)
        velocity_values_euler[next_time] = get_next_velocity_euler(time)
    
        height_values_trapezoidal[next_time] = get_next_height_trapezoidal(time)
        velocity_values_trapezoidal[next_time] = get_next_velocity_trapezoidal(time)
        
        time = next_time

        if height_values_trapezoidal[next_time] < MIN_HEIGHT and abs(velocity_values_trapezoidal[next_time]) < MIN_VELOCITY:
            break


def get_next_height_euler(t):
    return height_values_euler[t] + H * velocity_values_euler[t]

def get_next_velocity_euler(t):
    return velocity_values_euler[t] + H * get_acceleration(t)

def get_next_height_trapezoidal(t):
    return height_values_trapezoidal[t] + 0.5 * H * (velocity_values_trapezoidal[t] +  velocity_values_euler[t + H])

def get_next_velocity_trapezoidal(t):
    return velocity_values_trapezoidal[t] + 0.5 * H * (get_acceleration(t) + get_acceleration(t + H))


def get_acceleration(t):
    if height_values_euler[t] > 0: 
        return -ba/m * velocity_values_euler[t] - g
    if height_values_euler[t] <= 0:
        return -k/m * height_values_euler[t] - b/m * velocity_values_euler[t] - g



if __name__ == '__main__':
    run(method='euler')

    # Extract data to plot
    times_euler = list(height_values_euler.keys())
    heights_euler = list(height_values_euler.values())
    velocities_euler = list(velocity_values_euler.values())

    run(method='trapezoidal')
    times_trapezoidal = list(height_values_trapezoidal.keys())
    heights_trapezoidal = list(height_values_trapezoidal.values())
    velocities_trapezoidal = list(velocity_values_trapezoidal.values())

    # Create subplots
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

    # Save the plot to a file
    plt.savefig('simulation_plot.png')