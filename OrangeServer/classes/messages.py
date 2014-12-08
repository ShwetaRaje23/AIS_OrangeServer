import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


messages = [
    {
    "type":"Answer",
    "from":1,
    "to":2,
    "clueId":1
},
    {
    "type":"Question",
    "from":1,
    "to":2,
    "location":1
},
]

@csrf_exempt
def talk(request):
    if request.method == 'POST':
        return HttpResponse(json.dumps(messages), content_type="application/json")
    else:
        return HttpResponse(json.dumps(messages), content_type="application/json")