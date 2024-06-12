from integration_methods.euler import EulerMethod

class TrapezoidalMethod:

    def __init__(self, h):
        self.h = h
        self.euler_method = EulerMethod(h) 

    def compute_next_height(self, prev_height, prev_velocity, ba, m , b, g, k):
        result = prev_height + 0.5 * self.h * (prev_velocity + self.euler_method.compute_next_velocity(prev_height, prev_velocity, ba, m , b, g, k))
        return result
    
    def compute_next_velocity(self, prev_height, prev_velocity, ba, m , b, g, k):
        result = prev_velocity + 0.5 * self.h * (self.get_acceleration(prev_height, prev_velocity, ba, m , b, g, k) + self.euler_method.get_acceleration(prev_height, prev_velocity, ba, m , b, g, k))
        return result
    
    def get_acceleration(self, prev_height, prev_velocity, ba, m , b, g, k):
        if prev_height > 0: 
            return -ba / m * prev_velocity - g
        else:
            return -k / m * prev_height - b / m * prev_velocity - g