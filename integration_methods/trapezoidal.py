from integration_methods.euler import EulerMethod

class TrapezoidalMethod:

    """ def __init__(self, h, initial_height, initial_velocity):
        self.h = h
        self.height_values = {0: initial_height}
        self.velocity_values = {0: initial_velocity}
        self.euler_method = EulerMethod(h, initial_height, initial_velocity) """

    def __init__(self, h):
        self.h = h
        self.euler_method = EulerMethod(h) 

    def compute_next_height(self, prev_height, prev_velocity, ba, m , b, g, k):
        result = prev_height + 0.5 * self.h * (prev_velocity + self.euler_method.compute_next_velocity(prev_height, prev_velocity, ba, m , b, g, k))
        return result
    
    # return height_values_trapezoidal[t] + 0.5 * H * (velocity_values_trapezoidal[t] +  velocity_values_euler[t + H])

    def compute_next_velocity(self, prev_height, prev_velocity, ba, m , b, g, k):
        result = prev_velocity + 0.5 * self.h * (self.get_acceleration(prev_height, prev_velocity, ba, m , b, g, k) + self.euler_method.get_acceleration(prev_height, prev_velocity, ba, m , b, g, k))
        return result
    
    # return velocity_values_trapezoidal[t] + 0.5 * H * (get_acceleration(t) + get_acceleration(t + H))

    def get_acceleration(self, prev_height, prev_velocity, ba, m , b, g, k):
        if prev_height > 0: 
            return -ba / m * prev_velocity - g
        else:
            return -k / m * prev_height - b / m * prev_velocity - g



""" class TrapezoidalMethod:
    ba = 0.1    
    m = 1
    b = 30
    g = 9.8
    k = 100000

    def __init__(self, h, height_values, velocity_values):
        self.h = h
        self.height_values = height_values
        self.velocity_values = velocity_values
        self.euler_method = EulerMethod(h, height_values, velocity_values) 

    def __init__(self, h, initial_height, initial_velocity):
        self.h = h
        self.height_values = {0: initial_height}
        self.velocity_values = {0: initial_velocity}
        self.euler_method = EulerMethod(h, initial_height, initial_velocity)


    def compute_next_height(self, t):
        self.calculate_next_height_with_euler(t)
        self.calculate_next_velocity_with_euler(t)
        euler_velocity_next_step = self.euler_method.velocity_values[t + self.h]
        result = self.height_values[t] + 0.5 * self.h * (self.velocity_values[t] + euler_velocity_next_step) 

        self.height_values[t + self.h] = result
        return result
    

    def compute_next_velocity(self, t):
        result = self.velocity_values[t] + 0.5 * self.h * (self.get_acceleration(t) + self.get_acceleration_with_euler(t + self.h))
        self.velocity_values[t + self.h] = result
        return result


    def get_acceleration(self, t):
        if self.height_values[t] > 0: 
            return -self.ba / self.m * self.velocity_values[t] - self.g
        else:
            return -self.k / self.m * self.height_values[t] - self.b / self.m * self.velocity_values[t] - self.g


    def get_acceleration_with_euler(self, t):
        if self.height_values[t] > 0: 
            return -self.ba / self.m * self.euler_method.velocity_values[t] - self.g
        else:
            return -self.k / self.m * self.height_values[t] - self.b / self.m * self.euler_method.velocity_values[t] - self.g


    def calculate_next_height_with_euler(self, t):
        if t + self.h not in self.euler_method.height_values:
            self.euler_method.compute_next_height(t)


    def calculate_next_velocity_with_euler(self, t):
        if t + self.h not in self.euler_method.velocity_values:
            self.euler_method.compute_next_velocity(t) """