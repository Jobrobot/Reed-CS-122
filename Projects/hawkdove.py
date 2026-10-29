import random
import tkinter
random.seed()

def plot(xvals, yvals):
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') #was 350 x 280
    c.grid()
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

injurycost = 10   
displaycost = 1 
foodbenefit = 8 
init_hawk = 0
init_dove = 0
init_defensive = 0
init_evolving = 150

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
	def conflict(self, aot):
		for i in range(aot):
			if len(self.curbirds) < 2:
				break
			first, other = random.sample(self.curbirds, 2)
			first.encounter(other)
	def evolvingPlot(self):
		weights = []
		aggressiveness = []

		for bird in self.curbirds:
			if isinstance(bird, Evolving):
				weights.append(bird.weight)
				aggressiveness.append(bird.aggressiveness)

		plot(weights, aggressiveness)

	def status(self):
		print("Total birds:", len(self.curbirds))
		hawks = 0
		doves = 0
		defensive = 0
		evolving = 0

		for bird in self.curbirds:
			if bird.species == "Hawk":
				hawks += 1
			elif bird.species == "Dove":
				doves += 1
			elif bird.species == "Defensive":
				defensive += 1
			elif bird.species == "Evolving":
				evolving += 1

		print(f"There are {hawks} hawks and {doves} doves and {defensive} defensive birds and {evolving} evolving birds")
			
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
		if self.strat == True:
			other.eat()
		else:
			self.display()
			other.display()
			random.choice([self, other]).eat()
			
class Hawk(Bird):
	species = "Hawk"
	
	def update(self):
		super().update()
		if self.health >= 200:
			self.health -= 100
			Hawk(self.world)
	def defend_choice(self):
		return True
	def encounter(self, other):
		self.strat = other.defend_choice()
		if self.strat == False:
			self.eat()
		else:
			winner = random.choice([self, other])
			
			if winner is self:
				loser = other
			else:
				loser = self
				
			winner.eat()
			loser.injured()
			
class Defensive(Bird):
	species = "Defensive"
	def update(self):
		super().update()
		if self.health >= 200:
			self.health -= 100
			Defensive(self.world)
	defend_choice = Hawk.defend_choice
	encounter = Dove.encounter
			
class Evolving(Bird):
	species = "Evolving"

	def __init__(self, world, weight=None, aggressiveness=None):
		super().__init__(world)

		if weight is None:
			self.weight = random.uniform(1, 3)
		else:
			self.weight = weight + random.uniform(-0.1, 0.1)
			self.weight = max(1, min(3, self.weight))

		if aggressiveness is None:
			self.aggressiveness = random.uniform(0, 1)
		else:
			self.aggressiveness = aggressiveness + random.uniform(-0.05, 0.05)
			self.aggressiveness = max(0, min(1, self.aggressiveness))

	def defend_choice(self):
		return random.random() < self.aggressiveness

	def encounter(self, other):
		selff = self.defend_choice()
		otherf = other.defend_choice()

		if selff and otherf:
			win_probability = self.weight / (self.weight + other.weight)

			if random.random() < win_probability:
				winner, loser = self, other
			else:
				winner, loser = other, self

			winner.eat()
			loser.injured()

		elif selff:
			self.eat()

		elif otherf:
			other.eat()

		else:
			self.display()
			other.display()
			random.choice([self, other]).eat()

	def update(self):
		self.health -= 0.4 + 0.6 * self.weight

		if self.health <= 0:
			self.die()
		elif self.health >= 200:
			self.health -= 100
			Evolving(self.world, weight=self.weight, aggressiveness=self.aggressiveness)

w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w)

for t in range(10000):
    w.free_food(10) 
    w.conflict(50)
    w.update()
w.status()
w.evolvingPlot()


