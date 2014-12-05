import random

class Action:

	def __init__(self, name, actionid):
		#Display Related
		self.name = name
		self.actionid = actionid
		# self.characters_involved = [] #Which characters were involved in this action

	def actuallyPerformAction(self, location, objects, characters_involved):
		# print "Actually "
		actionDict = {
					"action": self.actionid,
					"characters_involved":[ch.characterId for ch in characters_involved],
					"objects_involved": [obj.objectid for obj in objects],
					"location": location.placeid,
					"display_string": "I " + self.name + "at" + location.name #"I spoke to ___ at ___"
				}

		if action.isActionPreconditionSatisfied(self,Game.globalSOW, location, objects, characters_involved):
			if self.name == 'Fight':
				probofaction = random.randint(0,1)
				if probofaction == 1:
					return [True,actionDict]
				else:
					return [False,actionDict]

			if self.name == 'See':
				return [True, actionDict]

			return [False, actionDict]

		else:



	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(self,player,SOW,location, objects, characters_involved):
		#return True

		if self.name == 'See':
			#does SOW have object in location?
			if len(player.current_location.object_in_location) > 0: 
				objis = player.current_location.object_in_location
				return True
			else if len(player.current_location.char_in_loc) > 1:
				player = player.current_location.char_in_loc
				return True
			else:
				return False  #need to return an action and person pair (not for see)
		 
		if self.name == 'Hear':
		 	for location in player.current_location.adjecent:
		 		for char in location.char_in_loc:
		 			if len(char.things_to_tell)>0:
		 				return True
		 	else:
		 		return False


		if self.name == 'Pick':			
		 	if len(player.current_location.object_in_location) > 0: 
				objis = player.current_location.object_in_location
		 		if objis in player.inventory == False: # how will you get the object detected?
		 			return True
		 	else:
		 		return False
        
        if self.name == 'Talk':
			if len(player.things_to_tell)>0:
				if len(player.current_location.char_in_loc)>0:
					return True
		 	else:
		 		return False

		 if self.name == 'Kill':				# you need to know who the person to be killed is?
		 	if objis in player.inventory:
		 		for objs in objis:
		 			if obj.isWeapon == True:
		 				if len(characters_involved)>0: 
		 					return True
		 				else:


		 	else:
		 		return False

		# if self.name == 'DropObject':
		#  	if has_object == True and object_to_be_dropped == True:
		#  		return True
		#  	else:
		#  		return False
        
		if self.name == 'Walk':
		 	return True
		 

		# 	return True
		# 	# if object_in_location or person_in_location:
		# 	# 	return True
		# 	# else:
		# 	# 	performAction('Walk')
        #
		# if self.name == 'Hear':
		# 	if person_in_adjecent_room > 1 and has_something_to_say(person) == True:
		# 		return True
		# 	else:
		# 		performAction('Walk')
        #
		# if self.name == 'Pick':
		# 	if obj_in_location == True and obj_in_inventory == False:
		# 		return True
		# 	else:
		# 		performAction('Walkto')
        #
		# if self.name == 'Kill':
		# 	if has_object == True and isWeapon == True and person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if self.name == 'Talk':
		# 	if has_something_to_say(person) == True and person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if self.name == 'DropObject':
		# 	if has_object == True and object_to_be_dropped == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if self.name == 'Walk':
		# 	return True

        # return True

#		if action == 'Fight':	 add later
			
	def performEffectsForAction(self):
		#Global state updated



		print ("Perform Effects For Action")