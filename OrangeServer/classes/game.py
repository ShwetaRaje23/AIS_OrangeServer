from action import Action
from stateofworld import StateOfWorld
from jsonparser import jsonParser

class Game:

	var = 0

	def __init__(self):

		[all_characters, all_objects, all_locations] = jsonParser.getGameParametersFromInputJSON("input.json")

		self.characters = all_characters
		self.objects = all_objects
		self.locations = all_locations
		self.globalSOW = StateOfWorld(all_locations,all_characters,all_objects) #Parse and return global SOW

	def tellMeAStory(self):
		#this is where the input values will come into the code.

		jsonResponse = []
		responseDict = {}

		#If stop condition not satisfied
		while not self.isStopConditionSatisfied():
			for character in self.characters:
				character.doActionLoop()

		#After Stop Condition satisfied
		print "Number of Characters =" ,len(self.characters)
		for character in self.characters:
			jsonResponse.append(character.getJSONFromKB())

		#Add KB to response
		responseDict['history'] = jsonResponse
		responseDict['locations'] = [loc.getJSON() for loc in self.locations]
		responseDict['characters'] = [ch.getJSON() for ch in self.characters]
		responseDict['objects'] = [obj.getJSON() for obj in self.objects]
		responseDict['victim'] = self.globalSOW.victim.characterId
		responseDict['killer'] = self.globalSOW.killer.characterId
		responseDict['motive'] = self.globalSOW.killer.motive #"Maid found the love letter between Wife and Secretary. Wife and Maid fought. Wife had a change of heart (or Wife decides to kill Maid)"

		return responseDict

	def isStopConditionSatisfied(self):

		# print Game.var
		if Game.var > 10:
			return True
		Game.var = Game.var+1
		return False


#Temp
game = Game()
game.tellMeAStory()
