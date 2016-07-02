import numpy as np

class vehicle:
    def __init__(self, width, length, height, weight, nWheels, maxSpeed, \
                 maxAccel, maxFuel, fuel, direction, x, y, vx, vy):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.nWheels = nWheels
        self.maxSpeed = maxSpeed
        self.maxAccel = maxAccel
        self.maxFuel = maxFuel
        self.fuel = fuel
        self.direction = direction
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.speed = np.sqrt(self.vx**2 + self.vy**2)

    def changePosition(self, accelX, accelY, dt):
        #for moving the vehicle, can be with or without acceleration        
        #kick velocity
        self.vx += (dt/2.0)*accelX
        self.vy += (dt/2.0)*accelY
        #drift position
        self.x += dt*self.vx
        self.y += dt*self.vy
        #kick velocity
        self.vx += (dt/2.0)*accelX
        self.vy += (dt/2.0)*accelY

        self.speed = np.sqrt(self.vx**2 + self.vy**2)

    def changeDirection(self):
        #did I ever figure this out for kerbacalc?
        pass

    def burnFuel(self, fuelBurnt):
        #could include decreasing weight by fuel amount
        #this all could be quite complicated if it wasn't me programming it
        self.fuel -= fuelBurnt

    def getOnHighway(self, start, end, dt):
        finalSpeed = 29.06
        speedDiff = finalSpeed - self.speed
        dist = np.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)
        accel = speedDiff**2/(2*dist)
        if accel > self.maxAccel:
            accel = self.maxAccel
            finalSpeed = np.sqrt(2*self.maxAccel*dist)
        dirMag = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        direction = np.array([end[0]-start[0], end[1]-start[1]])/dirMag
        while self.speed < finalSpeed:
            self.changePosition(accel*direction[0], accel*direction[1], dt)
