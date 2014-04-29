
class AbstractVehicle:
	def getSpeed(self):
		raise NotImplementedError, "getSpeed()"
	def getMake(self):
		raise NotImplementedError, "getMake()"
	def getModel(self):
		raise NotImplementedError, "getModel()"
	def getYear(self):
		raise NotImplementedError, "getYear()"
	def getColor(self):
		raise NotImplementedError, "getColor()"
	def getPower(self):
		raise NotImplementedError, "getPower()"
		
	def __init__(self):
		pass
		
	def engine(self, act):
		if act == "on":
			# if we have a fuel in tank turn it on
			if self.getTank() > 0:
				self.power = True
				return True
			return False
		elif act == "off":
			# power off engine only if the speed is 0 turn it off
			if self.getSpeed() == 0:
				self.power = False
				return True
			else:
				print "you can't power off engine when speed is " \
				+str(self.getSpeed())+"MPH"
		return False
				
	def accelerate(self):
		# if engine is on and we have a fuel in tank , start move 
		if self.power and self.getTank() > 0:
			self.speed += 5
			if self.getTank() > 0:
				self.tank -= 0.4
		else:
			print "you need first turn engine on or to fill tank"
			
	def brake(self):
		if self.getSpeed() > 0:
			self.speed -= 5
			
	def __str__(self):
		return "Make: "+self.getMake()+", Model: " \
				+self.getModel()+", Year: "+str(self.getYear()) \
				+", Color: "+self.getColor()