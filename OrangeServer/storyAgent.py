import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from classes.game import Game
from classes import messages

# @csrf_exempt
#     def dispatch(self, *args, **kwargs):
#         return super(MyView, self).dispatch(*args, **kwargs)

def playermessage(request,fromplayer,toplayer):
	return ""

@csrf_exempt
def tellMeAStory(request):
	#Reset messages
	messages.messages = []
	game = Game()
	Game.var = 0
	jsonResponse = game.tellMeAStory()

	return HttpResponse(json.dumps(jsonResponse), content_type="application/json")