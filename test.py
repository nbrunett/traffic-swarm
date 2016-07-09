import route
import vehicle

'''
car = vehicle.vehicle(7, 10, 5, 3200, 4, 30, 4, 12, 30, 0, 0, 0, 0, 0)

print car.x
print car.y
car.getOnHighway([car.x, car.y], [50, 50], 0.01)
print car.vx
print car.vy
print car.speed
'''

x = route.route(42.169002, -72.326345, 42.210410, -71.784496)
print x.coords.shape
print x.coords[0]
