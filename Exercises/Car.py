	import math
    
class Car:
	def __init__(self, mpg, max_tank, mic):
		self.mpg = mpg
		self.max_tank = max_tank
		self.tank = max_tank
		self.mic = mic
		self.x = 0
		self.y = 0
	def driveTo(self, x, y):
		distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
		if distance / self.mpg <= self.tank:
			self.tank -= distance / self.mpg
			self.x = x
			self.y = y
			return True
		else:
			return False
	def getLocation(self):
		current_location = [self.x, self.y]
		return current_location
	def getGas(self):
		return self.tank
	def getToFill(self):
		need_fuel = self.max_tank - self.tank
		return need_fuel
	def getMoney(self):
		return self.mic
	def pay(self, amount):
		self.mic -= amount
	def refill(self):
		self.tank = self.max_tank
		
class GasStation:
	def __init__(self, x, y, ppg):
		self.x = x
		self.y = y
		self.ppg = ppg
	def refillCar(self, car):
		x, y = car.getLocation()
		distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
		cost = car.getToFill() * self.ppg
		
		if distance > 0.001 or car.getMoney() < cost:
			return False
			
		car.pay(cost)
		car.refill()
		return True
		
class Taxi(Car):
	def __init__(self, mpg, max_tank, mic):
		super().__init__(mpg, max_tank, mic)
		self.pcount = 0
		self.miles = 0 
	def pickup(self):
		if self.pcount >= 1:
			return False
		else:
			self.pcount = 1
			self.miles = 0
			return True		
	def driveTo(self, x, y):
		distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
		
		if super().driveTo(x, y):
			if self.pcount == 1:
				self.miles += distance
			return True
		return False
		
	def dropoff(self):
		if self.pcount < 1:
			return False
		else:
			self.pcount -=1
			self.mic += self.miles * 3 + 2
			return True
class Dispatcher():
	def __init__(self):
		self.fleet = []
	
	def hire(self, taxi):
		self.fleet.append(taxi)
	def hail(self, x, y):
		closest_taxi = None
		closest_distance = float("inf")
		for i in self.fleet:
			taxix, taxiy = i.getLocation()
			distance = math.sqrt((x - taxix) ** 2 + (y - taxiy) ** 2)
			usage = distance / i.mpg
			if i.pcount == 0 and usage <= i.tank:
				if distance < closest_distance:
					closest_taxi = i
					closest_distance = distance
		if closest_taxi == None:
			return None
		closest_taxi.driveTo(x, y)
		closest_taxi.pickup()
		return closest_taxi
		
		
		
		