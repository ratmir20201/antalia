from django.shortcuts import render
from django.views.generic import ListView

from .models import Card, Message
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

messages = []  # Хранит сообщения в памяти (временно)


@csrf_exempt
def messages_view(request):
    if request.method == 'GET':
        return JsonResponse(messages, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        messages.append({
            'username': data.get('username'),
            'text': data.get('text'),
        })
        return JsonResponse({'status': 'ok'})


# def get_messages(request):
#     messages = Message.objects.order_by('timestamp')
#     data = [{"username": msg.username, "text": msg.text, "timestamp": msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for
#             msg in messages]
#     return JsonResponse(data, safe=False)
#
#
# @csrf_exempt
# def post_message(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         msg = Message.objects.create(username=data['username'], text=data['text'])
#         return JsonResponse({'status': 'ok', 'message': 'Сообщение отправлено'})


class ShopIndexView(ListView):
    template_name = "shopapp/index.html"
    model = Card
    context_object_name = "cards"
