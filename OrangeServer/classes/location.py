import random

class Location:

	def __init__(self, name, placeid, adjacent):
		self.name= name
		self.placeid = placeid
		self.adjacent=adjacent
		self.objects_in_loc= []
		self.char_in_loc=[]
 	
 	def update_from_SOW(self):
 		# needed to update from the sow at every instance to see who is where
		return True

	def getJSON(self):
		return {
			"name":self.name,
			"placeid":self.placeid,
			"adjacent":[loc.getJSON() for loc in self.adjacent],
			"objects_in_loc":[obj.getJSON() for obj in self.objects_in_loc],
			"characters_in_loc":[ch.getJSON() for ch in self.char_in_loc]
		}