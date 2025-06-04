from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from django.conf import settings

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

        return JsonResponse({'message': 'Email sent successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    return HttpResponse("Hello from contact app!")