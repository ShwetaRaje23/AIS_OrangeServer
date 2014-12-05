class Action:

	def __init__(self, name, actionid):
		#Display Related
		self.name = name
		self.actionid = actionid
		# self.characters_involved = [] #Which characters were involved in this action

	def actuallyPerformAction(self, location, objects, characters_involved):
		print (" Loop to perform actions ")
		# make all characters perform all actions and some of them will be satisfied based on the pre-conditions
		# initial loop makes characters perform all actions or just see hear and walk - TODO
		#

		#take a characterid and write his/her trajectory
		#
		if self.name == 'See':
			# objectsSeen = ""
			# for obj in objects:
			# 	objectsSeen = objectsSeen + obj.name
			#
			actionDict = {
					"action": self.name,
					"characters_involved":[ch.characterId for ch in characters_involved],
					"objects_involved": [obj.objectid for obj in objects],
					"location": location.placeid,
					"display_string": "I " + self.name + "at" + location.name #"I spoke to ___ at ___"
				}
			return [True, actionDict]


		print "Action was not performed successfully"
		# return [fail, instacen of Goal]


	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(action):
		return True
		#returns a boolean depending on weather the precondition of the action was satisfied
		# if action == 'See':
		# 	#try to satisfy pre-conditions
		# 	print ("In see action")
		# 	# Here we need to code from the other classes like, Location here.
		# 	# these variables will be set from a global state of the world.
		# 	# The main classes will get updated as well as update the global state of the world
		# 	#
		# 	if object_in_location == True or person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if action == 'Hear':
		# 	if person_in_adjecent_room > 1 and has_something_to_say(person) == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if action == 'Pick':
		# 	if obj_in_location == True and obj_in_inventory == False:
		# 		return True
		# 	else:
		# 		return False
        #
		# if action == 'Kill':
		# 	if has_object == True and isWeapon == True and person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if action == 'Talk':
		# 	if has_something_to_say(person) == True and person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if action == 'DropObject':
		# 	if has_object == True and object_to_be_dropped == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if action == 'Walk':
		# 	return True
        #

#		if action == 'Fight':	 add later
			
	def performEffectsForAction(self):
		#Global state updated


		print ("Perform Effects For Action")