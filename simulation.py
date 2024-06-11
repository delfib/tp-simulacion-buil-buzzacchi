
MAX_TIME = 100
MIN_HEIGHT = 0.00001
MIN_VELOCITY = 0.0001

class Simulation:
    def __init__(self, method, initial_height, initial_velocity, h):
        self.time = 0
        self.h = h
        self.height_values = {self.time: initial_height}
        self.velocity_values = {self.time: initial_velocity}
        self.method = method(h)

    def run(self):
        while self.time <= MAX_TIME:
            next_time = self.time + self.h

            prev_height = self.height_values[self.time]
            prev_velocity = self.velocity_values[self.time]

            self.height_values[next_time] = self.method.compute_next_height(prev_height, prev_velocity)
            self.velocity_values[next_time] = self.method.compute_next_velocity(prev_height, prev_velocity)

            self.time = next_time

            if (self.height_values[next_time] < MIN_HEIGHT and 
                abs(self.velocity_values[next_time]) < MIN_VELOCITY):
                break

        return self.height_values, self.velocity_values
