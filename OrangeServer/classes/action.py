import random
from  thingtotell import ThingToTell
from goal import Goal

class Action:

	def __init__(self, name, actionid):
		#Display Related
		self.name = name
		self.actionid = actionid
		# self.characters_involved = [] #Which characters were involved in this action

	def actuallyPerformAction(self, player, location, objects, characters_involved):

		from game import Game
		# print "Actually "
		#Make charcters_involved = other_characters_incolved
		characters_involved = [ch for ch in characters_involved if ch.characterId != player.characterId]
		actionDict = {
					"action": self.actionid,
					"characters_involved":[ch.characterId for ch in characters_involved],
					"objects_involved": [obj.objectid for obj in objects],
					"location": location.placeid,
					"display_string": "I " + self.name + "at" + location.name #"I spoke to ___ at ___"
				}#TODO : improve display string
		ch = characters_involved[0] if len(characters_involved)>0 else None

		if self.isActionPreconditionSatisfied(player, Game.globalSOW, location, objects, characters_involved):
			print player.name, " did ", self.name, " at ", location.name , " with ", [ch.name for ch in characters_involved] , " and ", [obj.name for obj in location.objects_in_location] ,"and has inventory", [obj.name for obj in player.inventory]

			#Special conditions
			if self.name == 'Talk':

				if len(player.things_to_tell)>0:
					for thing_to_tell in player.things_to_tell:
						people_about_whom = []
						people_about_whom = people_about_whom + [ch for ch in thing_to_tell.chars_involved]
						people_about_whom = people_about_whom + [ch for ch in [obj.people_involved for obj in thing_to_tell.objs_involved]]

						chars_in_adj = []
						for adj in player.current_location.adjacent:
							for chr in adj.char_in_loc:
								chars_in_adj.append(chr)

						for ch in chars_in_adj:
							if ch in people_about_whom:
								#Update actionDict to add to knowledge base
								actionDict['characters_involved'] = [ch.characterId]
								actionDict['action'] = 8 #Fight actionid hardcode TODO: remove

								fightAction = Action('Fight',8)
								player.goals.append(Goal(fightAction,people_about_whom,thing_to_tell))

								print "FIGHT ! (add to kb. Also create goal)"
								return [True, actionDict]

			return [True, actionDict]

		else:
			return [False, actionDict]


	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(self,player,SOW,location, objects, characters_involved):

		from game import Game
		if self.name == 'Talk':
			if len(player.things_to_tell)>0:
				for thing_to_tell in player.things_to_tell:
					people_about_whom = []
					people_about_whom = people_about_whom + [ch for ch in thing_to_tell.chars_involved]
					people_about_whom = people_about_whom + [ch for ch in [obj.people_involved for obj in thing_to_tell.objs_involved]]

					# print people_about_whom

					if len(player.current_location.char_in_loc)<0:
						return False
					else:
						for ch in player.current_location.char_in_loc:
							if ch in people_about_whom:
								return False #Do not talk if the person is in the room

						for ch in player.current_location.char_in_loc:
							ch.things_to_tell.append(thing_to_tell)

						#Characters in adjacent rooms overhearing current char
						chars_in_adj = []
						for adj in player.current_location.adjacent:
							for chr in adj.char_in_loc:
								chars_in_adj.append(chr)

						for ch in chars_in_adj:
							if ch in people_about_whom:
								return True
							else:
								ch.things_to_tell.append(thing_to_tell)
					return False
			else:
				return False


		if self.name == 'Fight':
			return True


		if self.name == 'See':
			#does SOW have object in location?
			other_char_in_loc = [ch.name for ch in player.current_location.char_in_loc if ch.name != player.name]
			if len(player.current_location.objects_in_location) > 0:
				return True
			elif len(other_char_in_loc) > 0:
				#Add person to things_to_say
				print "HAS SOMETHING TO SAY"
				thing_to_tell = ThingToTell(self,other_char_in_loc,[])
				player.things_to_tell.append(thing_to_tell)
				return True
			else:
				return False  #need to return an action and person pair (not for see)

		if self.name == 'Pick':
			other_char_in_loc = [ch.name for ch in player.current_location.char_in_loc if ch.name != player.name]
			if len(player.current_location.objects_in_location) > 0:
				for objis in player.current_location.objects_in_location:
					if not objis in player.inventory:
						if not objis.is_weapon or (objis.is_weapon and player.motive != ""):
							# Add object to things_to_say
							print "HAS SOMETHING TO SAY"
							thing_to_tell = ThingToTell(self,random.sample(Game.globalSOW.all_characters,min(2,len(Game.globalSOW.all_characters))),[objis])
							player.things_to_tell.append(thing_to_tell)

							#Drop other item
							if len(player.inventory) >0:
								player.current_location.objects_in_location.append(player.inventory.pop(0))

							#Pick up new object
							player.inventory.append(objis)
							player.current_location.objects_in_location.remove(objis)
							break #pick one object only
						else:
							print "Player cannot pick up weapon"
				return True
			else:
				return False

		if self.name == 'Kill':		# you need to know who the person to be killed is?
			for obj in player.inventory:
				if obj.is_weapon == True:
					if len(characters_involved)>0:
						character_to_kill = characters_involved[0]
						if character_to_kill.current_location == player.current_location:
							return True
						else:
							#Go to character_to_kill's location
							print ""
					else:
						print ""
			return False

		if self.name == 'Walk':
			new_loc = random.choice(player.current_location.adjacent)
			player.current_location.char_in_loc.remove(player)
			player.current_location = new_loc
			player.current_location.char_in_loc.append(player)
			return True



	def performEffectsForAction(self,player,SOW,location, objects, characters_involved):
		print ("Perform Effects For Action")
