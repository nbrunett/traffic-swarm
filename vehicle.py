import numpy as np

transFric = 0.1

class vehicle:
    def __init__(self, width, length, height, weight, nWheels, maxSpeed, \
                 maxAccel, maxFuel, fuel, fric, direction, pos, vel):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.nWheels = nWheels
        self.maxSpeed = maxSpeed
        self.maxAccel = maxAccel
        self.maxFuel = maxFuel
        self.fuel = fuel
        self.fric = fric
        self.direction = direction #north of east; radians
        self.pos = pos
        self.vel = vel
        self.speed = np.linalg.norm(self.vel)


    def changePosition(self, accel, dt):
        #calculate parallel drag (e.g. "air drag")
        dirVec = np.array([np.cos(self.direction), np.sin(self.direction)])
        parVel = np.dot(self.vel, dirVec)
        parDrag = -parVel*dirVec*self.fric

        #calculate transverse drag
        if dirVec[0] == 0.0:
            perp = np.array([1.0, -dirVec[0]/dirVec[1]])
        else:
            perp = np.array([-dirVec[1]/dirVec[0], 1.0])
        perp /= np.linalg.norm(perp)
        transVel = np.dot(self.vel, perp)
        transDrag = -transVel*perp*transFric

        #kick velocity
        accel = np.array(accel)
        self.vel += (dt/2.0)*accel + parDrag + transDrag
        #drift position
        self.pos += dt*self.vel
        #kick velocity
        self.vel += (dt/2.0)*accel + parDrag + transDrag

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
