import numpy as np

class vehicle:
    def __init__(self, width, length, height, weight, nWheels, maxSpeed, \
                 maxAccel, maxFuel, fuel, direction, pos, vel):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.nWheels = nWheels
        self.maxSpeed = maxSpeed
        self.maxAccel = maxAccel
        self.maxFuel = maxFuel
        self.fuel = fuel
        self.direction = direction #north of east
        self.pos = pos
        self.vel = vel
        self.speed = np.linalg.norm(self.vel)

    def changePosition(self, accel, dt):
        #for moving the vehicle, can be with or without acceleration        
        #kick velocity
        self.vel[0] += (dt/2.0)*accel[0]
        self.vel[1] += (dt/2.0)*accel[1]
        #drift position
        self.pos[0] += dt*self.vel[0]
        self.pos[1] += dt*self.vel[1]
        #kick velocity
        self.vel[0] += (dt/2.0)*accel[0]
        self.vel[1] += (dt/2.0)*accel[1]

        self.speed = np.linalg.norm(self.vel)

    def changeDirection(self, delDirection):
        self.direction += delDirection

    def burnFuel(self, fuelBurnt):
        #could include decreasing weight by fuel amount
        #this all could be quite complicated if it wasn't me programming it
        self.fuel -= fuelBurnt

    def getOnHighway(self, start, end, dt):
        finalSpeed = 29.06
        speedDiff = finalSpeed - self.speed
        dist = np.linalg.norm(start-end)
        accel = speedDiff**2/(2.0*dist)
        if accel > self.maxAccel:
            accel = self.maxAccel
            finalSpeed = np.sqrt(2.0*self.maxAccel*dist)
        dirMag = np.linalg.norm(end-start)
        direction = np.array([end[0]-start[0], end[1]-start[1]])/dirMag
        while self.speed < finalSpeed:
            self.changePosition([accel*direction[0], accel*direction[1]], dt)
