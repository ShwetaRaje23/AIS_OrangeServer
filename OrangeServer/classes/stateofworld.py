import random
import json
from character import Character
from object import Object
from location import Location

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

		#Parse input file
		[all_characters, all_objects] = self.getGameParameteresFromJSON("input.json")

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

	#JSON Parser
	def getGameParameteresFromJSON(self,filepath):

		filedata = open(filepath)
		jsonData = json.load(filedata)

		characters = jsonData['characters']
		locations = jsonData['locations']
		objects = jsonData['objects']

		all_characters = []
		all_objects = []

		for character in characters:
			name = character['name']
			charid = character['characterid']
			charDesc = character['characterDescription']

			all_characters.append(Character(name,charid,charDesc))

		for location in locations:
			name = location['name']
			placeid = location['placeid']
			adj = location['adjacent_places']

			self.locations.append(Location(name,placeid,adj))

		#Now set adj locations by id
		for location in self.locations:
			adjloc = []
			for locindex in location.adjacent:
				loc = filter(lambda l:l.placeid == locindex,self.locations)
				if len(loc)>0:
					adjloc.append(loc[0])
			location.adjacent = adjloc

		for object in objects:
			name = object['name']
			objectid = object['objectid']
			is_weapon = object['is_weapon']
			after_use = object['after_use']

			all_objects.append(Object(name,objectid,is_weapon,after_use))

		return [all_characters, all_objects]

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