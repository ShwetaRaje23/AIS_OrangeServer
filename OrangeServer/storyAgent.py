
def tellMeAStory():
	return HttpResponse(json.dumps({'tellMeAStory': 'Story'}), "application/json")