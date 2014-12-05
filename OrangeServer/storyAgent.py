import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from classes.game import Game

@csrf_exempt
def playermessage(request,fromplayer,toplayer):
	return ""

@csrf_exempt
def tellMeAStory(request):

	game = Game()
	Game.var = 0
	jsonResponse = game.tellMeAStory()

	return HttpResponse(json.dumps(jsonResponse), "application/json")