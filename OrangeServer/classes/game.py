from action import Action
from stateofworld import StateOfWorld

class Game:

	def __init__(self):
		self.characters = []
		self.globalSOW = StateOfWorld() #Parse and return global SOW

	def tellMeAStory(self):
		#this is where the input values will come into the code.

		#If stop condition not satisfied

		#For each character
		#character.doActionLoop()


		#After Stop Condition satisfied
		#For each Character
		#Character.getJSONFromKnowledgeBase

		#For parameter in game.SOW
		#Add parameter to JSON

		print ('Start Simulation')
		return {'tellMeAStory': 'Story'}