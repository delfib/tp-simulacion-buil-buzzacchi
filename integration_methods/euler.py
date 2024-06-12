class EulerMethod:
    
    def __init__(self, h):
        self.h = h

    def compute_next_height(self, prev_height, prev_velocity, ba, m , b, g, k):
        result = prev_height + self.h * prev_velocity
        return result

    def compute_next_velocity(self, prev_height, prev_velocity, ba, m , b, g, k):
        result = prev_velocity + self.h * self.get_acceleration(prev_height, prev_velocity, ba, m , b, g, k)
        return result

    def get_acceleration(self, prev_height, prev_velocity, ba, m , b, g, k):
        if prev_height > 0: 
            return -ba / m * prev_velocity - g
        else:
            return -k / m * prev_height - b / m * prev_velocity - g