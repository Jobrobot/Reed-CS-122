import random

class World():
	def __init__(self):
		self.curbirds = []
	def update(self):
		for bird in self.curbirds.copy():
			bird.update()
	def free_food(self, noff):
		for i in range(noff):
			Bird.eat(random.choice(self.curbirds))
	def conflict(aot):
		for i in range(aot):
			first = random.randrange(self.curbirds)
			bring_back = self.curbirds.pop(first)
			other.encounter(random.choice(self.curbirds))
			self.curbirds.insert(bring_back, first)
	def status(self):
		for bird in self.curbirds:
			if "Hawk" in self.curbirds:
				self.hawks += 1
			elif "Dove" in self.curbirds:
				self.doves += 1
		
		print(f" There are {self.hawks} hawks and {self.doves} doves")
			
class Bird():
	def __init__(self, world):
		self.health = 100
		self.world = world
		world.curbirds.append(self)
	def eat(self):
		self.health += foodbenefit
	def injured(self):
		self.health -= injurycost
	def display(self):
		self.health -= displaycost
	def die(self):
		self.world.curbirds.remove(self)
	def update(self):
		self.health -= 1
		if self.health <= 0:
			self.die()
class Dove(Bird):
	species = "Dove"
	
	def update(self):
		super().update()
		if self.health >= 200:
			self.health -= 100
			Dove(self.world)
	def defend_choice(self):
		return False
	def encounter(self, other):
		self.strat = other.defend_choice()
		if self.strat == False:
			Bird.eat(random.choice([self, other]))
		else:
			Bird.eat(other)
			
		
class Hawk(Bird):
	species = "Hawk"
	
	def update(self):
		super().update()
		if self.health >= 200:
			self.health -= 100
			Hawk(self.world)
	def defend_choice():
		return True
	def encounter(self, other):
		self.strat = other.defend_choice()
		if self.strat == False:
			Bird.eat(self)
		else:
			chosen_bird = random.choice([self, other])
			chosen_bird.eat()
			chosen_bird.injured()


init_hawk = 50
init_dove = 50
init_defence = 0
init_evolving = 0
injurycost = 11
displaycost = 1
goodbenefit = 11
				