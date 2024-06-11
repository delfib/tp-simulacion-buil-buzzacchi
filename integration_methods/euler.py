class EulerMethod:
    ba = 0.1   
    m = 1
    b = 30
    g = 9.8
    k = 100000
    
    def __init__(self, h, initial_height, initial_velocity):
        self.h = h
        self.height_values = {0: initial_height}
        self.velocity_values = {0: initial_velocity}

    def compute_next_height(self, t):
        result = self.height_values[t] + self.h * self.velocity_values[t]
        self.height_values[t + self.h] = result
        return result

    def compute_next_velocity(self, t):
        result = self.velocity_values[t] + self.h * self.get_acceleration(t)
        self.velocity_values[t + self.h] = result
        return result

    def get_acceleration(self, t):
        if self.height_values[t] > 0: 
            return -self.ba / self.m * self.velocity_values[t] - self.g
        else:
            return -self.k / self.m * self.height_values[t] - self.b / self.m * self.velocity_values[t] - self.g