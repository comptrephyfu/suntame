class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

# Define vectors a and b
a = Vector(3, 4)
b = Vector(1, 2)

# Assume a.r and b.r are the magnitudes of vectors a and b
a_r = a.magnitude()
b_r = b.magnitude()

# Calculate ab as the dot product of a and b
ab = a.x * b.x + a.y * b.y

# Using the provided formula to calculate dx
dx = (a.x * b_r + b.x * a_r) / ab

print(f"dx = {dx}")
