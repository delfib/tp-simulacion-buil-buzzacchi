class EulerMethod:
    ba = 0.1   
    m = 1
    b = 30
    g = 9.8
    k = 100000
    
    def __init__(self, h):
        self.h = h

    def compute_next_height(self, prev_height, prev_velocity):
        result = prev_height + self.h * prev_velocity
        return result

    def compute_next_velocity(self, prev_height, prev_velocity):
        result = prev_velocity + self.h * self.get_acceleration(prev_height, prev_velocity)
        return result

    def get_acceleration(self, prev_height, prev_velocity):
        if prev_height > 0: 
            return -self.ba / self.m * prev_velocity - self.g
        else:
            return -self.k / self.m * prev_height - self.b / self.m * prev_velocity - self.g