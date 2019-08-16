from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import Algorithmia

#client = Algorithmia.client('simGBUPXKvkvvjWFTf/VxTy9P2l1')
#algo = client.algo('dysfunctionalbot/Hello/0.1.0')
#client = Algorithmia.client('simGBUPXKvkvvjWFTf/VxTy9P2l1')
#algo = client.algo('dysfunctionalbot/Jokes/0.1.1')
client = Algorithmia.client('simGBUPXKvkvvjWFTf/VxTy9P2l1')
algo = client.algo('dysfunctionalbot/Jokes/0.2.1')

algo.set_options(timeout=300) # optional


@csrf_exempt
def get_response(request):
    response = {'status': None}
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        chat_response = algo.pipe(message).result
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
        #response['message'] = {'text': 'response', 'user': False, 'chat_bot': True}
        response['status'] = 'ok'
    else:
        response['error'] = 'no post data found'
    return HttpResponse(
        json.dumps(response),
            content_type="application/json")


def home(request, template_name="home.html"):
    context = {'title': 'Dysfunctional bot Version 1.0'}
    return render_to_response(template_name, context)
