class Character:

	def __init__(self):
		#Display oriented
		self.name = ""
		self.characterDescription = ""
		self.motive = ""

		#Story Oriented
		self.inventory = []
		self.personality = []
		self.things_to_tell = []
		self.myKB = None
		self.goals = []
		self.current_location = None


		#initialize actions for character
	# action = 'See'
	# 		if Action.isActionPreconditionSatisfied(action):
	# 			#pirnt the below and also add to the KB as clue
	# 			#print ('charater', characterid , 'did action', action, 'at' , time, 'in' locationid)
	# 		else:
	# 			#find out what is needed to get to satisfy the action (not always true) only when its a goal
    #
    #
	# 		action = 'Hear'
	# 		Action.isActionPreconditionSatisfied(action)
    #
	# 		action = 'Pick'
	# 		Action.isActionPreconditionSatisfied(action)
    #
	# 		action = 'Walk'
	# 		Action.isActionPreconditionSatisfied(action)

	def performAction(self,action):

		#If is_preconfition_Satisfied()
		#[success, ret] = action.performAction()


		#Perform Effects of action
		#If success, add ret to self.knowedge
		#If success = false, add ret to goal
		#Update local and global SOW

		print "Perform Action"

	def doActionLoop(self):

		#For action in every_turn_action (see. hear, walk)
		#self.performAction(action)

		#



		print "Do Action Loop"

