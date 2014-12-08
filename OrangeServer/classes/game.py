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
			print "STOP CONDITION NOT SATISFIED"
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
		responseDict['victim'] = self.globalSOW.victim.characterId if self.globalSOW.victim else -1
		responseDict['killer'] = self.globalSOW.killer.characterId if self.globalSOW.killer else -1
		responseDict['motive'] = ""#self.globalSOW.killer.motive #"Maid found the love letter between Wife and Secretary. Wife and Maid fought. Wife had a change of heart (or Wife decides to kill Maid)"



		return responseDict

	def isStopConditionSatisfied(self):

		# print "CHECK STOP CONDITION", Game.globalSOW.killer.name if Game.globalSOW.killer else "",Game.globalSOW.victim.name if Game.globalSOW.victim else ""
		if Game.globalSOW.killer is None:
			if Game.var > 20:
				print " ************************* "
				return True
			return False
		else:
			print " :):):):):):):):):):):):):):):):)"
			return True


		#If there is a murderer or victim
		# 	return False

		# if Game.var > 20:
		# 	return True
		# Game.var = Game.var+1
		# return False


#Temp
# game = Game()
# game.tellMeAStory()
