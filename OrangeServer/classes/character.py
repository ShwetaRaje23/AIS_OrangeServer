from action import Action
# from game import Game
import random

class Character:

	def __init__(self, name, characterDescription, characterId,all_actions=[]):
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
		self.all_actions = all_actions

		#Action Related
		self.current_location = None

	def getJSONFromKB(self):
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

		[success, ret] = action.actuallyPerformAction(self, self.current_location, self.current_location.objects_in_location, self.current_location.char_in_loc)
		if success:
			self.myKB.append(ret)
		# else:
		# 	self.goals.append(ret)

	def doActionLoop(self):

		for action in self.all_actions:
			if not(action.name == 'Fight' or action.name == 'Kill'):
				# print self.name ,"perform action", action.name, " ",action.actionid
				self.performAction(action)

		for goal in self.goals:

			# print "I HAVE A GOAL TO", goal.action.name

			if goal.action.name == 'Fight':
				probofaction = random.randint(0,1)
				shouldFight = True
				if probofaction == 1:
					shouldFight = True
				else:
					shouldFight = False

				killaction = Action('Kill',4)
				from goal import Goal

				motiveString = self.name + " found the "+ goal.thing_to_tell.objs_involved[0].name+ " between "+ goal.people_involved[0].name + " and "+ goal.people_involved[1].name+"."
				print "MOTIVE: ",motiveString

				if shouldFight:
					#Fight between self and character
					print "Kill between",goal.people_involved[0].name, "and", self.name, "because of", [obj.name for obj in goal.thing_to_tell.objs_involved]
					killer = goal.people_involved[0]
					victim = self
					killer.motive = motiveString
					killer.goals.append(Goal(killaction,[victim],goal.thing_to_tell))

				else:
					killer = goal.people_involved[1]
					victim = goal.people_involved[0]
					killer.motive = motiveString + victim.name + " had a change of heart."
					killer.goals.append(Goal(killaction,[victim],goal.thing_to_tell))
					print "Kill between",goal.people_involved[0].name, "and", goal.people_involved[1].name, "because of", [obj.name for obj in goal.thing_to_tell.objs_involved]

				self.goals.remove(goal)

			elif goal.action.name == 'Kill':
				killer = self
				victim = goal.people_involved[0]

				hasWeapon = False
				for obj in self.inventory:
					if obj.is_weapon:
						hasWeapon = True
						break

				chars_in_locations = []
				for char in self.current_location.char_in_loc:
					chars_in_locations.append(char)
				for adj in self.current_location.adjacent:
					for char in adj.char_in_loc:
						chars_in_locations.append(char)

				if victim in chars_in_locations and hasWeapon:
					from game import Game
					Game.globalSOW.victim = victim
					Game.globalSOW.killer = killer

					print victim.name , killer.name
					print "KILL !"
					self.goals.remove(goal)
					# exit(0)
					return True

	def getJSON(self):
		return {
			"name":self.name,
			"characterid":self.characterId,
			"characterDescription":self.characterDescription,
			"motive":self.motive
		}