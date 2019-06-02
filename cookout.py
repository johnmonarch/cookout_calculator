import math
import numpy as np

i = 1
cookout_flavors = 46
combos = 0
total_shakes = 0

while i <= cookout_flavors:
	combos = (math.factorial(cookout_flavors))/(math.factorial(i)*(math.factorial(cookout_flavors - i)))
	total_shakes = total_shakes + combos
	i += 1

print(total_shakes)

