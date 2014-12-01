class Action:

	def __init__(self):
		#Display Related
		self.name = ""
		self.characters_involved = [] #Which characters were involved in this action

	#
	# Does this person satisfy the preconditions of this action ?
	# If not, tell the person to do those actions
	# 
	def isPreconditionSatisfied(person):
		print ("Is Precondition Satisfied")
		
	def performAction(self):
		print (" Loop to perform actions ")
		# make all characters perform all actions and some of them will be satisfied based on the pre-conditions
		# initial loop makes characters perform all actions or just see hear and walk - TODO
		#

		#take a characterid and write his/her trajectory
		#

		action = 'See'
		Action.isActionPreconditionSatisfied(action)


	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(action):
		#returns a boolean depending on weather the precondition of the action was satisfied
		if action == 'See':
			#try to satisfy pre-conditions
			print ("In see action")
			if object_in_location == True or person_in_location == True:
				return True
			else:
				return False

		if action == 'Hear':
			if person_in_adjecent_room > 1 and has_something_to_say(person) == True:
				return True
			else:
				return False

		if action == 'Pick':
			if obj_in_location == True and obj_in_inventory == False:
				return True
			else:
				return False

		if action == 'Kill':
			if has_object == True and isWeapon == True and person_in_location == True:
				return True
			else:
				return False

		if action == 'Talk':
			if has_something_to_say(person) == True and person_in_location == True:
				return True
			else:
				return False	

		if action == 'DropObject':
			if has_object == True and object_to_be_dropped == True:
				return True
			else:
				return False

		if action == 'Walk':
			return True


#		if action == 'Fight':	 add later
			
	def performEffectsForAction():
		print ("Perform Effects For Action")