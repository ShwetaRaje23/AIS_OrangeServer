import json
from character import Character
from object import Object
from location import Location

class jsonParser:

    @classmethod
    def getGameParametersFromInputJSON(self,filepath):

		filedata = open(filepath)
		jsonData = json.load(filedata)

		characters = jsonData['characters']
		locations = jsonData['locations']
		objects = jsonData['objects']

		all_characters = []
		all_objects = []
		all_locations = []

		for character in characters:
			name = character['name']
			charid = character['characterid']
			charDesc = character['characterDescription']

			all_characters.append(Character(name,charid,charDesc))

		for location in locations:
			name = location['name']
			placeid = location['placeid']
			adj = location['adjacent_places']

			all_locations.append(Location(name,placeid,adj))

		#Now set adj locations by id
		for location in all_locations:
			adjloc = []
			for locindex in location.adjacent:
				loc = filter(lambda l:l.placeid == locindex,all_locations)
				if len(loc)>0:
					adjloc.append(loc[0])
			location.adjacent = adjloc

		for object in objects:
			name = object['name']
			objectid = object['objectid']
			is_weapon = object['is_weapon']
			after_use = object['after_use']

			all_objects.append(Object(name,objectid,is_weapon,after_use))

		return [all_characters, all_objects, all_locations]