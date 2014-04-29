import vehicle_python as Vehicle

class Car(Vehicle.AbstractVehicle):
	def __init__(self, make, model, year, color):
		Vehicle.AbstractVehicle.__init__(self)
		self.speed = 0
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.power = False 
		self.tank = 0.0
		self.tank_capacity = 50.0 # litres
		
	def getTank(self):
		return self.tank
		
	def getTankCapacity(self):
		return self.tank_capacity
		
	def setTank(self, fuel):
		empty = self.getTankCapacity() - self.getTank()
		#print "empty in tank : "+str(empty)
		if (self.getTank() == 0 and fuel < self.getTankCapacity()):
			self.tank = fuel	
		elif (empty < fuel):
			self.tank = 50.0
			#print "to much: "+str(fuel - empty)
		else:
			self.tank += fuel
			
	def getSpeed(self):
		return self.speed
		
	def getMake(self):
		return self.make
		
	def getModel(self):
		return self.model
		
	def getYear(self):
		return self.year
		
	def getColor(self):
		return self.color
		
	def getPower(self):
		return self.power