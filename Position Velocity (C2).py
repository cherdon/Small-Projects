def position_velocity(v, t):
    my_v = v
    my_t = t
    g = 9.81

    return round(my_v * my_t - (1 / 2) * (g) * (my_t ** 2),2), round(my_v - g * (my_t),2)


v = float(input("What is your initial velocity?"))
t = float(input("What is the time at t?"))
output = position_velocity(v, t)
velocity,acceleration = position_velocity(v,t)
print(velocity, acceleration)
