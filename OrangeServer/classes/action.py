import random

class Action:

	def __init__(self):
		#Display Related
		self.name = ""
		self.characters_involved = [] #Which characters were involved in this action

	#
	# Does this person satisfy the preconditions of this action ?
	# If not, tell the person to do those actions
	# 
	def isPreconditionSatisfied(self,person):
		print ("Is Precondition Satisfied")
	

	# give probability for actions (for onw only works on fight)
	# can be used to give probability for possible other action
	#	
	def performAction(self):
		print (" Loop to perform actions ")
		if self.name == 'Fight':
			probofaction = random.randint(0,1)
			if probofaction == 1:
				return True
			else:
				return False
		#if we want probabilistic actions to be performed
		return True

		# make all characters perform all actions and some of them will be satisfied based on the pre-conditions
		# initial loop makes characters perform all actions or just see hear and walk - TODO
		#

		#take a characterid and write his/her trajectory
		#

		# if self.name == 'See':
		# 	print self.characters_involved, "saw" 
		# 	# return  [success, instance of knowledge base]
		# if self.name == 'Hear':
		# 	print self.characters_involved, "hear" 
		# if self.name == 'Talk':
		# 	print self.characters_involved, "talk"
		# if self.name == 'Pick':
		# 	print self.characters_involved, "pick"
		# if self.name == 'Kill':
		# 	print self.characters_involved, "kill"

			
		# return [fail, instacen of Goal]


	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(action):
		#returns a boolean depending on weather the precondition of the action was satisfied
		if action == 'See':
			#try to satisfy pre-conditions
			print ("In see action")
			# Here we need to code from the other classes like, Location here.
			# these variables will be set from a global state of the world.
			# The main classes will get updated as well as update the global state of the world
			#
			if object_in_location or person_in_location:
				return True
			else:
				performAction('Walk')

		if action == 'Hear':
			if person_in_adjecent_room > 1 and has_something_to_say(person) == True:
				return True
			else:
				performAction('Walk')

		if action == 'Pick':
			if obj_in_location == True and obj_in_inventory == False:
				return True
			else:
				performAction('Walkto')

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