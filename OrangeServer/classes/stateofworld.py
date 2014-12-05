import random

class StateOfWorld:
#instead of this, the flow can have these things in the specific classes and other classes can just read that info
# eg: If i need to know before hear or see action the people in the room, I can query the location class.
#
	def __init__(self,all_locations,all_characters,all_objects):

		#Information about Game World
		self.locations = all_locations

		#Information about character roles
		self.victim = None
		self.killer = None

		#Set initial conditions
		self.place_characters_randomly(all_characters)
		self.place_objects_randomly(all_objects)

		self.printSOW()

	def printSOW(self):
		print "STATE OF THW WORLD"

		for loc in self.locations:
			print "\n ---------------- ", loc.name, " ---------------- "
			for loc2 in loc.adjacent:
				print loc2.name," ",

			print ""
			for obj in loc.objects_in_loc:
				print obj.name, " ",

			print ""
			for ch in loc.char_in_loc:
				print ch.name," ",

	#Initialize character positions, etc
	def place_characters_randomly(self, characters):
		#
		# place characters in different places.
		# depending on this the SOW of the world would get initialized.
		# assigning the characterid to a random location id
		#
		for char in characters:
			randLoc = random.choice(self.locations)
			randLoc.char_in_loc.append(char)
		#
		# for characterid in range(1,6):
		# 	person_in_location = random.randint(1,8)
		# 	print (characterid, 'is at location' , person_in_location )

	def place_objects_randomly(self, objects):
		# place objects in random locations
		#  be sure to update the state of the world and also knowledge base
		#

		for obj in objects:
			randLoc = random.choice(self.locations)
			randLoc.objects_in_loc.append(obj)

		# for objectid in range(1,9):
		# 	obj_in_location = random.randint(1,8)
		# 	print (objectid, 'in location' , obj_in_location )

	#def give_personality_vector():	- TODO: later
