import random
from  thingtotell import ThingToTell

class Action:

	def __init__(self, name, actionid):
		#Display Related
		self.name = name
		self.actionid = actionid
		# self.characters_involved = [] #Which characters were involved in this action

	def actuallyPerformAction(self, player, location, objects, characters_involved):
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

		from game import Game
		if self.isActionPreconditionSatisfied(player, Game.globalSOW, location, objects, characters_involved):
			print player.name, " did ", self.name, " at ", location.name , " with ", ch.name if ch else "" , " and ", [obj.name for obj in location.objects_in_location] ,"and has inventory", [obj.name for obj in player.inventory]
			if self.name == 'Fight':
				probofaction = random.randint(0,1)
				if probofaction == 1:
					return [True,actionDict]
				else:
					return [False,actionDict]

			if self.name == 'See':
				return [True, actionDict]

			return [False, actionDict]

		else:
			return [False, actionDict]


	#give preconditions based on the action performed in an if else loop
	def isActionPreconditionSatisfied(self,player,SOW,location, objects, characters_involved):

		if self.name == 'See':
			#does SOW have object in location?
			other_char_in_loc = [ch.name for ch in player.current_location.char_in_loc if ch.name != player.name]
			if len(player.current_location.objects_in_location) > 0:
				return True
			elif len(other_char_in_loc) > 0:
				#Add person to things_to_say
				thing_to_tell = ThingToTell(self,other_char_in_loc,[])
				player.things_to_tell.append(thing_to_tell)
				return True
			else:
				return False  #need to return an action and person pair (not for see)
		 
		if self.name == 'Hear':
			for location in player.current_location.adjacent:
				for char in location.char_in_loc:
					if len(char.things_to_tell)>0:
						return True
					else:
						return False

		if self.name == 'Pick':			
			if len(player.current_location.objects_in_location) > 0:
				for objis in player.current_location.objects_in_location:
					if not objis in player.inventory:
						if not objis.is_weapon:
							print "Picked up", objis.name

							# Add object to things_to_say
							thing_to_tell = ThingToTell(self,[],[objis])
							player.things_to_tell.append(thing_to_tell)
							player.inventory.append(objis)
							player.current_location.objects_in_location.remove(objis)
							break #pick one object only
						else:
							print "Need to handle is_weapon"
				return True
			else:
				return False
        
		if self.name == 'Talk':
			if len(player.things_to_tell)>0:

				for thing_to_tell in player.things_to_tell:
					people_about_whom = []
					people_about_whom = [ch for ch in thing_to_tell.chars_involved]
					people_about_whom = people_about_whom + [ch for ch in thing_to_tell.objs_inolved.people_involved]

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
							chars_in_adj.append(adj.char_in_location)

						for ch in chars_in_adj:
							if ch in people_about_whom:
								print "FIGHT FIGHT FIGHT"
								#or update motive
							else:
								ch.things_to_tell.append(thing_to_tell)

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
				# else:
				# 	return False

		# if self.name == 'DropObject':
		#  	if has_object == True and object_to_be_dropped == True:
		#  		return True
		#  	else:
		#  		return False
        
		if self.name == 'Walk':
			player.current_location = random.choice(location.adjacent)
			return True
		 

		# 	return True
		# 	# if objects_in_location or person_in_location:
		# 	# 	return True
		# 	# else:
		# 	# 	performAction('Walk')
        #
		# if self.name == 'Hear':
		# 	if person_in_adjecent_room > 1 and has_something_to_say(person) == True:
		# 		return True
		# 	else:
		# 		performAction('Walk')
        #
		# if self.name == 'Pick':
		# 	if obj_in_location == True and obj_in_inventory == False:
		# 		return True
		# 	else:
		# 		performAction('Walkto')
        #
		# if self.name == 'Kill':
		# 	if has_object == True and isWeapon == True and person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if self.name == 'Talk':
		# 	if has_something_to_say(person) == True and person_in_location == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if self.name == 'DropObject':
		# 	if has_object == True and object_to_be_dropped == True:
		# 		return True
		# 	else:
		# 		return False
        #
		# if self.name == 'Walk':
		# 	return True

        # return True

#		if action == 'Fight':	 add later
			
	def performEffectsForAction(self,player,SOW,location, objects, characters_involved):
		
		#Global state updated



		print ("Perform Effects For Action")
