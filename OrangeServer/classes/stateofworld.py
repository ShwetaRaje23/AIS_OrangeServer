import random

class StateOfWorld:
#instead of this, the flow can have these things in the specific classes and other classes can just read that info
# eg: If i need to know before hear or see action the people in the room, I can query the location class.
#
	def __init__(self):
		
		#Information about Game World
		self.locations = []

		#Information about character roles
		self.victim = None
		self.killer = None

	#JSON Parser
	def getGameParameteresFromJSON(self,filepath):
		return True

	#Initialize character positions, etc
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
