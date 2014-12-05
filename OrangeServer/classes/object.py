class Object:
	
	def __init__(self, name, objectid, is_weapon, after_use):
		self.name= name
		self.objectid = objectid
		self.is_weapon= is_weapon
		self.after_use= after_use
		self.is_used= False

	def canPick(self,person):
		#check if a person can pick a particular object or not. return bool. 
		return True

	def getJSON(self):
		return {
			"name":self.name,
			"objectid":self.objectid,
			"is_weapon":self.is_weapon,
			"after_use":self.after_use,
			"is_used":self.is_used
		}

