import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from classes.game import Game



def tellMeAStory(request):

	game = Game()
	Game.var = 0
	jsonResponse = game.tellMeAStory()

	return HttpResponse(json.dumps(jsonResponse), "application/json")