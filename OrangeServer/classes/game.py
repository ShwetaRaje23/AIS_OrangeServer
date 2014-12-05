from stateofworld import StateOfWorld
from jsonparser import jsonParser
import os

class Game:

	var = 0
	globalSOW = None

	def __init__(self):

		#Get input JSON
		module_dir = os.path.dirname(__file__)  # get current directory
		file_path = os.path.join(module_dir, "input.json")
		[all_characters, all_objects, all_locations, all_actions] = jsonParser.getGameParametersFromInputJSON(file_path)

		self.characters = all_characters
		self.objects = all_objects
		self.locations = all_locations
		Game.globalSOW = StateOfWorld(all_locations,all_characters,all_objects) #Parse and return global SOW

	def tellMeAStory(self):
		#this is where the input values will come into the code.

		jsonResponse = []
		responseDict = {}

		#If stop condition not satisfied
		while not self.isStopConditionSatisfied():
			for character in self.characters:
				character.doActionLoop()

		#After Stop Condition satisfied
		for character in self.characters:
			knowledge = character.getJSONFromKB()
			for piece in knowledge:
				jsonResponse.append(piece)

		#Add KB to response
		responseDict['history'] = jsonResponse
		responseDict['locations'] = [loc.getJSON() for loc in self.locations]
		responseDict['characters'] = [ch.getJSON() for ch in self.characters]
		responseDict['objects'] = [obj.getJSON() for obj in self.objects]
		responseDict['victim'] = 1#self.globalSOW.victim.characterId
		responseDict['killer'] = 2#self.globalSOW.killer.characterId
		responseDict['motive'] = "Some motive text here"#self.globalSOW.killer.motive #"Maid found the love letter between Wife and Secretary. Wife and Maid fought. Wife had a change of heart (or Wife decides to kill Maid)"

		return responseDict

	def isStopConditionSatisfied(self):

		#If there is a murderer or victim
		if Game.globalSOW.victim and Game.globalSOW.killer:
			return True
		return False


		# print Game.var
		if Game.var > 5:
			return True
		Game.var = Game.var+1
		return False


#Temp
# game = Game()
# game.tellMeAStory()
