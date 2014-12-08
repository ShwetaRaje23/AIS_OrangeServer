import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

messages = []

# messages = [
#     {
#     "type":"Answer",
#     "from":1,
#     "to":2,
#     "clueId":1
# },
#     {
#     "type":"Question",
#     "from":1,
#     "to":2,
#     "location":1
# },
# ]

@csrf_exempt
def ask(request):
    if request.method == 'POST':
        msgtype = "Question"
        msgfrom = request.POST["from"]
        msgto = request.POST["to"]
        msglocation = request.POST['location']

        messages.append({
            "type":msgtype,
            "from":msgfrom,
            "to":msgto,
            "location":msglocation
        })
    return HttpResponse(json.dumps(messages), content_type="application/json")

@csrf_exempt
def answer(request):
    if request.method == 'POST':
        msgtype = "Answer"
        msgfrom = request.POST["from"]
        msgto = request.POST["to"]
        msgclueid = request.POST['clueId']

        messages.append({
            "type":msgtype,
            "from":msgfrom,
            "to":msgto,
            "clueId":msgclueid
        })

    return HttpResponse(json.dumps(messages), content_type="application/json")

@csrf_exempt
def checkMessages(request):
    return HttpResponse(json.dumps(messages), content_type="application/json")