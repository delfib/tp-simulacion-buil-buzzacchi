
MAX_TIME = 100
MIN_HEIGHT = 0.00001
MIN_VELOCITY = 0.0001

class Simulation:
    def __init__(self, method, initial_height, initial_velocity, h):
        self.time = 0
        self.h = h
        self.method = method(h, {self.time: initial_height}, {self.time: initial_velocity})

    def run(self):
        while self.time <= MAX_TIME:
            next_time = self.time + self.h

            self.method.compute_next_height(self.time)
            self.method.compute_next_velocity(self.time)

            self.time = next_time

            if (self.method.height_values[next_time] < MIN_HEIGHT and 
                abs(self.method.velocity_values[next_time]) < MIN_VELOCITY):
                break

        return self.method.height_values, self.method.velocity_values