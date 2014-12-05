from action import Action
# from game import Game

class Character:

	def __init__(self, name, characterDescription, characterId):
		#Display oriented
		self.name = name
		self.characterId = characterId
		self.characterDescription = characterDescription
		self.motive = ""

		#Story Oriented
		self.inventory = []
		self.personality = []
		self.things_to_tell = []
		self.myKB = []
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

	@classmethod
	def allActions(cls):
		actions = []
		for action in ['See','Hear','Pick']:
			actions.append(Action(action,len(actions)))
		return actions

	def getJSONFromKB(self):

		#Parse

		# [
		#	OUTPUT JSON STRUCTURE:
		# 	{
		# 		iteration: 1,
		# 		time: "9:00"
		# 		action_name: 'see',
		# 		action_id: 2,
		# 		performed_on: [1], #everyone but me
		# 		performed_by: 2,
		# 		objects_involved: [3],
		# 		location:7
		# 	}
		# ]


		'''
			[
				{
					"action":action_object
					"characters_involved":[character_object]
					"objects_involved": [object_object]
					"location":location_object
					"display_string":"I spoke to ___ at ___"
				}
			]
		'''

		print "*******", len(self.myKB)
		myKnowledge = []
		for piece in self.myKB:
			knowledge = {
				"iteration": 1,
				"time": "9:00",
				# "action_name": 'see',
				"action_id": piece["action"],
				"performed_on": piece["characters_involved"], #everyone but me
				"performed_by": self.characterId,
				"objects_involved": piece["objects_involved"],
				"location":piece["location"]
			}
			myKnowledge.append(knowledge)

		return myKnowledge

	def performAction(self,action):

		from game import Game
		if action.isActionPreconditionSatisfied():
			[success, ret] = action.actuallyPerformAction(Game.globalSOW.locations[0], [], [])
			if success:
				self.myKB.append(ret)
			else:
				self.goals.append(ret)

		#[success, ret] = action.actuallyPerformAction()
		#If success, add ret to self.knowedge if not walk, etc
		#If success = false, add ret to goal ret = [highest_level_action_to_perform, characters_involved]

	def doActionLoop(self):
		for action in Character.allActions():
			self.performAction(action)

	def getJSON(self):
		return {
			"name":self.name,
			"characterid":self.characterId,
			"characterDescription":self.characterDescription,
			"motive":self.motive
		}