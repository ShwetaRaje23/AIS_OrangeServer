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

		if self.name == 'Fight':
			probofaction = random.randint(0,1)
			if probofaction == 1:
				return [True,actionDict]
			else:
				return [False,actionDict]

		if self.name == 'See':
			return [True, actionDict]

		return [False, actionDict]

	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(self,player,SOW):

		# if self.name == 'See':
		# 	object_in_location =
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

        return True

#		if action == 'Fight':	 add later
			
	def performEffectsForAction(self):
		#Global state updated


		print ("Perform Effects For Action")