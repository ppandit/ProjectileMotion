'''
   Draw the trajectory of a body in projectile motion
'''
from matplotlib import pyplot as plt
import math


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_graph_with_args(x, y, u, theta):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    s = 'Projectile motion of a ball ' + 'velocity = ' + str(u) + ' angle = ' + str(round(theta))
    plt.title(s)

'''
Generate equally spaced floating-point
numbers between two given values
'''

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

def draw_trajectory(u, theta):
    rad_theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2 * u * math.sin(rad_theta) / g
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(rad_theta) * t)
        y.append(u * math.sin(rad_theta) * t - 0.5 * g * t * t)

    #draw_graph(x, y)
    draw_graph_with_args(x,y,u,theta)


if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()