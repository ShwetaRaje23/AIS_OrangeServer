import random
from action import Action

class Game:

	def __init__(self):
		self.characters = []
		self.globalSOW= None

	def tellMeAStory(self):
		#this is where the input values will come into the code.
		print ('Start Simulation')
		
	def place_characters_randomly(self):
		#
		# place characters in different places.
		# depending on this the SOW of the world would get initialized.
		# assigning the characterid to a random location id
		#

		for characterid in range(1,6):
			person_in_location = random.randint(1,8)
			print (characterid, 'is at location' , person_in_location )
		
	def place_objects_randomly(self):
		# place objects in random locations
		#  be sure to update the state of the world and also knowledge base
		#

		for objectid in range(1,9):
			obj_in_location = random.randint(1,8)
			print (objectid, 'in location' , obj_in_location )
	
	#def give_personality_vector():	- TODO: later		

objOfGame = Game()
objOfGame.tellMeAStory()
objOfGame.place_characters_randomly()
objOfGame.place_objects_randomly()

objOfAction = Action()
objOfAction.performAction()
#x.person_in_location
