# Task 2: Using the Math Module for Calculations
import math
n = int(input('Enter a number: '))
def fn(n):
    square_root = math.sqrt(n)
    print('Square root :',square_root)
    natural_log = math.log(n)
    print('Logarithm :',natural_log)
    #angle_radians = math.pi/2
    sine_value = math.sin(math.radians(n))
    print('Sine : ',sine_value)

fn(n)