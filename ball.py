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
height_values = {}
velocity_values = {}


def run():
    time = 0
    height_values[time] = 10
    velocity_values[time] = 0

    while time <= MAX_TIME:
        next_time = time + H
        height_values[next_time] = get_next_height(time)
        velocity_values[next_time] = get_next_velocity(time)

        time = next_time

        if height_values[next_time] < MIN_HEIGHT and abs(velocity_values[next_time]) < MIN_VELOCITY:
            break


def get_next_height(t):
    return height_values[t] + H * velocity_values[t]


def get_next_velocity(t):
    return velocity_values[t] + H * get_acceleration(t)


def get_acceleration(t):
    if height_values[t] > 0: 
        return -ba/m * velocity_values[t] - g
    if height_values[t] <= 0:
        return -k/m * height_values[t] - b/m * velocity_values[t] - g


run()