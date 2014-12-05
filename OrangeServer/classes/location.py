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

