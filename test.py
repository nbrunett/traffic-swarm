import matplotlib.pyplot as plt
import numpy as np

import route
import vehicle

car = vehicle.vehicle(7, 10, 5, 3200, 4, 31.29, 9.8, 12, 12, 0.0, np.pi/4.0, \
                      [0, 0], [10, 20])

print car.pos
car.getOnHighway(car.pos, np.array([50, 50]), 0.01)
print car.vel
print car.speed


x = route.route(42.170350, -72.479596, 42.210243, -71.784453)
plt.plot(x.coords[:, 0], x.coords[:, 1])
plt.scatter(x.coords[:, 0], x.coords[:, 1])
plt.show()
