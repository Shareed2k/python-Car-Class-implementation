import unittest2
import car_python as CarClass

class CarTest(unittest2.TestCase):
	
	def setUp(self):
		self.carObj = CarClass.Car("Toyota", "Corolla", 2009, "Red")
		
	def test_speed_when_engine_off(self):	
		self.failUnlessEqual(self.carObj.getSpeed(), 0)
		
	def test_engine_on_full_gas(self):
		# lats fill full tank 50 litres
		self.carObj.setTank(50.0)
		self.carObj.engine("on")
		for i in range(32): # 160MPH
			self.carObj.accelerate()
		self.failUnlessEqual(self.carObj.getSpeed(), 160)
		
	def test_car_model(self):
		self.failUnlessEqual(self.carObj.getModel(), "Corolla")
		
	# let's test if we can power off engine when car is in move #
	def test_power_off_engine_on_the_drive(self):
		self.carObj.setTank(50.0)
		self.carObj.engine("on")
		for i in range(32): # 160MPH
			self.carObj.accelerate()
			
		self.failIf(self.carObj.engine("off"))
		
	def test_brake(self):
		self.carObj.setTank(50.0)
		self.carObj.engine("on")
		for i in range(32): # 160MPH
			self.carObj.accelerate()
			
		# push the brake
		for i in range(12):  # 100MPH
			self.carObj.brake()
			
		self.failUnlessEqual(self.carObj.getSpeed(), 100)
		
	def test_tank_capacity(self):
		# lats fill full tank 50 litres
		self.carObj.setTank(50.0)
		self.carObj.engine("on")
		for i in range(32): # 160MPH
			self.carObj.accelerate()
			
		self.failUnlessAlmostEqual(37, self.carObj.getTank(), places=0)

if __name__ == '__main__':
		unittest2.main()