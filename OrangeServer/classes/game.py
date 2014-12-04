from action import Action
from stateofworld import StateOfWorld

class Game:

	def __init__(self):
		self.characters = []
		self.globalSOW = StateOfWorld() #Parse and return global SOW

	def tellMeAStory(self):
		#this is where the input values will come into the code.

		jsonResponse = []

		#If stop condition not satisfied
		if not self.isStopConditionSatisfied():
			for character in self.characters:
				character.doActionLoop()
		else:
			#After Stop Condition satisfied
			for character in self.characters:
				jsonResponse.append(character.getJSONFromKB())

		#Add KB to response
		jsonResponse['history'] = jsonResponse


		#For parameter in game.SOW
		#Add parameter to JSON

		print ('Start Simulation')
		return {'tellMeAStory': 'Story'}

	def isStopConditionSatisfied(self):



		return False


#Temp
game = Game()
game.tellMeAStory()
