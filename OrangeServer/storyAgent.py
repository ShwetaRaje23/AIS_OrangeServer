import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



def tellMeAStory(request):
	return HttpResponse(json.dumps({'tellMeAStory': 'Story1'}), "application/json")